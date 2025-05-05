from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/ainur-aldiyar-toiga-shaqyru", response_class=HTMLResponse)
async def read_invite(request: Request):
    return templates.TemplateResponse("invite.html", {"request": request})
