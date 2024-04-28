import os

import aiohttp

from exception.not_found_exception import NotFoundException
from scheme.double_gis_response_scheme import DoubleGisResponse
from scheme.point_scheme import Point


async def get_point(point_address: str) -> Point:
    double_gis_api_key = os.getenv("DOUBLE_GIS_API_KEY")
    if double_gis_api_key is None:
        raise EnvironmentError("Variable DOUBLE_GIS_API_KEY is not found in .env file.")

    async with aiohttp.ClientSession() as session:
        params = {
            "q": point_address,
            "fields": "items.point",
            "key": double_gis_api_key,
        }
        async with session.get(
            f"https://catalog.api.2gis.com/3.0/items/geocode", params=params
        ) as response:
            response = DoubleGisResponse.model_validate_json(await response.text())

    if response.meta.error:
        raise NotFoundException("Point is not found.")

    return Point(
        address=point_address,
        latitude=response.result.items[0].point.lat,
        longitude=response.result.items[0].point.lon,
        is_cache=False,
    )
