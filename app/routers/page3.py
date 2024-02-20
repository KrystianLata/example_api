from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("page3.html", {"request": request})
