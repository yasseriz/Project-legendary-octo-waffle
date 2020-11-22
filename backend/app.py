from fastapi import FastAPI, Request
from backend.routes.series import router as seriesRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./frontend/")

app = FastAPI()

app.include_router(seriesRouter, tags=["Series"], prefix="/series")

@app.get("/", tags=["Root"])
async def read_root(request: Request):
    message = "Welcome"
    return templates.TemplateResponse("main.html",context={"request":request,"message":message})

