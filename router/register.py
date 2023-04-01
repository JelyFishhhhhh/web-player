from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from aiofiles import open as aopen
from modules import method, genVCODE

router = APIRouter(tags=["user"])

@router.get("/register")
async def register():

    async with aopen ("templates/register.html", "rb") as html_file:

        return HTMLResponse(await html_file.read())

@router.post("/register")
async def register(
        username:str = Form(...), 
        email:str = Form(...), 
        password: str = Form(...),
        confirm_password: str = Form(...)
    ):

    await method.sql_insert(name=username, email=email, password=password)
    return RedirectResponse(url="/login", status_code=303)