from backend.models.schema import (
    ErrorResponseModel,
    ResponseModel,
    DataSchema,
    updateDataSchema,
)
from backend.database import (
    addSeries,
    getSeries,
    deleteSeries,
    updateSeries,
)
from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./frontend/")


router = APIRouter()


@router.post("/", response_description="Series data added into database")
async def addSeriesData(request: Request):
    form = await request.form()
    seriesJSON = jsonable_encoder(form)
    newSeries = await addSeries(seriesJSON)
    series = await getSeries()
    return templates.TemplateResponse("main.html", context={"request": request, "message": "Series added successfully", "series": series})


@router.get("/", response_description="Series retrieved")
async def getSeriesData(request: Request):
    series = await getSeries()
    if series:
        return templates.TemplateResponse("main.html", context={"request": request, "message": "Series data retrieved successfully", "series": series})
    return templates.TemplateResponse("main.html", context={"request": request, "message": "Empty list returned"})


@router.post("/{id}", response_description="Series data deleted from database")
async def deleteSeriesData(id: str, request: Request):
    deletedSeries = await deleteSeries(id)
    series = await getSeries()
    if deletedSeries:
        # return ResponseModel(
        #     "Series with ID: {} removed".format(
        #         id), "Series deleted successfully"
        # )
        return templates.TemplateResponse("main.html", context={"request": request, "message": "Series with ID: {} removed".format(id), "series": series})
    # return ErrorResponseModel(
    #     "An error occurred", 404, "Series with id {0} doesn't exist".format(id)
    # )
    return templates.TemplateResponse("main.html", context={"request": request, "message": "Series with id {0} doesn't exist".format(id), "series": series})


@router.post("/update/{id}")
# async def updateSeriesData(id: str, req: updateDataSchema = Body(...)):
async def updateSeriesData(request:Request, id:str):
    form = await request.form()
    seriesJSON = jsonable_encoder(form)
    updatedSeries = await updateSeries(id, seriesJSON)
    series = await getSeries()
    if updatedSeries:
        return templates.TemplateResponse("main.html", context={"request": request, "message": "Series with ID: {} updated".format(id), "series": series})
        # return ResponseModel(
        #     "Series with ID: {} name update is successful".format(id),
        #     "Series name updated successfully",
        # )
    return templates.TemplateResponse("main.html", context={"request": request, "message": "Series with id {0} doesn't exist".format(id), "series": series})
    # return ErrorResponseModel(
    #     "An error occurred",
    #     404,
    #     "There was an error updating the series data.",
    # )
