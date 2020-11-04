from fastapi import FastAPI
from backend.routes.series import router as seriesRouter

app = FastAPI()

app.include_router(seriesRouter, tags=["Series"], prefix="/series")

@app.get("/", tags=["Root"])
async def read_root():
    message = {"message":"Welcome"}
    return message

