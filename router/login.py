from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from aiofiles import open as aopen
from modules import genVCODE, method, User_Profile

router = APIRouter(tags=["user"])

@router.get("/login")
async def login():

    async with aopen ("templates/login.html", "rb") as html_file:
    
        return HTMLResponse(await html_file.read())
    
@router.post("/login")
async def login(username:str  = Form(...), password:str = Form(...)):

    user = await method.sql_where_by_NAME(User_Profile, name=username)
    
    if user is None:
        return {"Message" : {"user not founded"}}
    
    elif user.password != password:
        return {"Message" : {"password error"}}
    
    else:
        print(f">>>Login as \n->{username}")
        return RedirectResponse(url="/", status_code=303)
