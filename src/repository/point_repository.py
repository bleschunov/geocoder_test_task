from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection
from asyncpg.types import Point as PostgresPoint

from exception.not_found_exception import NotFoundException
from scheme.point_scheme import Point, PointUpload


async def get_similar_point(point: PointUpload, db: AsyncConnection) -> Point:
    response = await db.execute(
        text(
            "SELECT address, coords, similarity(point.address, :address) sml "
            "FROM point WHERE point.address % :address ORDER BY sml LIMIT 1"
        ),
        {"address": point.address},
    )
    result = response.fetchone()

    if not result:
        raise NotFoundException("Similar points are not found.")

    return Point(
        address=result.address,
        latitude=result.coords.x,
        longitude=result.coords.y,
        is_cache=True,
    )


async def save_point(point: Point, db: AsyncConnection) -> Point:
    await db.execute(
        text("INSERT INTO point (address, coords) VALUES (:address, :point)"),
        {
            "address": point.address,
            "point": PostgresPoint(point.latitude, point.longitude),
        },
    )
