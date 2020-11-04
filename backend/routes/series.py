from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.database import (
    addSeries,
    getSeries,
)

from backend.models.schema import (
    ErrorResponseModel,
    ResponseModel,
    DataSchema,
    updateDataSchema
)

router = APIRouter()

@router.post("/", response_description="Series data added into database")
async def addSeriesData(series: DataSchema = Body(...)):
    series = jsonable_encoder(series)
    newSeries = await addSeries(series)
    return ResponseModel(newSeries, "Series added successfully")

@router.get("/", response_description="Students retrieved")
async def getSeriesData():
    series = await getSeries()
    if series:
        return ResponseModel(series, "Students data retrieved successfully")
    return ResponseModel(series, "Empty list returned")