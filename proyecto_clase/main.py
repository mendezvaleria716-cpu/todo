from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# Crear la aplicación
app = FastAPI()
app.mount ("/imagenes",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def inicio(request: Request):
    return templates.TemplateResponse(name="index.html",
                                      request=request,
                                      context={"Nombre":"Edwars"})