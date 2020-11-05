from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from backend.database import (
    addSeries,
    getSeries,
    deleteSeries,
    updateSeries,
)

from backend.models.schema import (
    ErrorResponseModel,
    ResponseModel,
    DataSchema,
    updateDataSchema,
)

router = APIRouter()


@router.post("/", response_description="Series data added into database")
async def addSeriesData(series: DataSchema = Body(...)):
    series = jsonable_encoder(series)
    newSeries = await addSeries(series)
    return ResponseModel(newSeries, "Series added successfully")


@router.get("/", response_description="Series retrieved")
async def getSeriesData():
    series = await getSeries()
    if series:
        return ResponseModel(series, "Series data retrieved successfully")
    return ResponseModel(series, "Empty list returned")


@router.delete("/{id}", response_description="Series data deleted from database")
async def deleteSeriesData(id: str):
    deletedSeries = await deleteSeries(id)
    if deletedSeries:
        return ResponseModel(
            "Series with ID: {} removed".format(
                id), "Series deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Series with id {0} doesn't exist".format(id)
    )


@router.put("/{id}")
async def updateSeriesData(id: str, req: updateDataSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updatedSeries = await updateSeries(id, req)
    if updatedSeries:
        return ResponseModel(
            "Series with ID: {} name update is successful".format(id),
            "Series name updated successfully",
        )

    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the series data.",
    )
