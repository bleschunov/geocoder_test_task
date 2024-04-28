from fastapi import APIRouter, Depends, HTTPException

from exception.not_found_exception import NotFoundException
from infra.db import get_conn
from model import geocoder_model
from scheme.point_scheme import PointRead, PointUpload

router = APIRouter()


@router.post("/address/", tags=["address"], response_model=PointRead)
async def read_users(point: PointUpload, db=Depends(get_conn)):
    try:
        return await geocoder_model.get_point_by_address(point, db)
    except NotFoundException:
        raise HTTPException(status_code=404, detail="Point is not found.")


