from scheme.base_model import BaseModel


class PointUpload(BaseModel):
    address: str


class PointRead(PointUpload):
    latitude: float
    longitude: float
    is_cache: bool


class Point(PointRead):
    pass
