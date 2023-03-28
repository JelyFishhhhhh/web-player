from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from aiofiles import open as aopen

router = APIRouter(tags=["home"])

@router.get("/")
async def home():
    async with aopen ("templates/index.html", mode="rb") as html_file:

        return HTMLResponse(await html_file.read())
