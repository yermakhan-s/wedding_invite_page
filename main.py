from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# 🔒 Middleware to skip ngrok splash warning
@app.middleware("http")
async def skip_ngrok_warning(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["ngrok-skip-browser-warning"] = "true"
    return response

@app.get("/ainur-aldiyar-toiga-shaqyru", response_class=HTMLResponse)
async def read_invite(request: Request):
    return templates.TemplateResponse("invite.html", {"request": request})
