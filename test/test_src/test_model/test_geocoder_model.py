import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__),
    '../../../src/')
))

from unittest import IsolatedAsyncioTestCase

from dotenv import load_dotenv

from exception.not_found_exception import NotFoundException
from model import geocoder_model
from repository import point_repository
from scheme.point_scheme import Point, PointUpload


class TestGeocoderModel(IsolatedAsyncioTestCase):
    async def test_getting_point_from_cache(self):
        load_dotenv(".env.test")
        from infra.db import engine

        async with engine.begin() as db:
            await point_repository.save_point(Point(address="большая черемушкинская 20", latitude=55.55, longitude=55.55, is_cache=False), db)

            point = await geocoder_model.get_point_by_address(PointUpload(address="б черемушкинская 20"), db)

        assert point.is_cache is True

    async def test_getting_point_from_api(self):
        load_dotenv(".env.test")
        from infra.db import engine

        async with engine.begin() as db:
            point = await geocoder_model.get_point_by_address(PointUpload(address="москва садовническая 21"), db)

        assert point.is_cache is False

    async def test_exception_404_if_point_is_not_found(self):
        load_dotenv(".env.test")
        from infra.db import engine

        async with engine.begin() as db:
            with self.assertRaises(NotFoundException):
                await geocoder_model.get_point_by_address(PointUpload(address="..."), db)


if __name__ == "__main__":
    unittest.main()
