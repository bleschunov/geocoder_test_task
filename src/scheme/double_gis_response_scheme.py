from scheme.base_model import BaseModel


class DoubleGisResponseError(BaseModel):
    message: str
    type: str


class DoubleGisResponseMeta(BaseModel):
    api_version: str
    code: int
    error: DoubleGisResponseError = None
    issue_date: str


class DoubleGisPoint(BaseModel):
    lat: float
    lon: float


class DoubleGisResponseResultItem(BaseModel):
    point: DoubleGisPoint


class DoubleGisResponseResult(BaseModel):
    items: list[DoubleGisResponseResultItem]
    total: int


class DoubleGisResponse(BaseModel):
    meta: DoubleGisResponseMeta
    result: DoubleGisResponseResult = None
