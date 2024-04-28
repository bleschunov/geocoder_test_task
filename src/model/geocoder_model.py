from sqlalchemy.ext.asyncio import AsyncConnection

from exception.not_found_exception import NotFoundException
from infra import double_gis_api
from repository import point_repository
from scheme.point_scheme import PointUpload, Point


async def get_point_by_address(point: PointUpload, db: AsyncConnection) -> Point:
    try:
        return await point_repository.get_similar_point(point, db)
    except NotFoundException:
        pass

    point = await double_gis_api.get_point(point.address)

    await point_repository.save_point(point, db)
    return point
