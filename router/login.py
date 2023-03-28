from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from aiofiles import open as aopen

router = APIRouter(tags=["user"])

@router.get("/login")
async def login():

    async with aopen ("templates/login.html", "rb") as html_file:
    
        return HTMLResponse(await html_file.read())
    
@router.post("/login")
async def login(username:str  = Form(...), password:str = Form(...)):

    print(f">>>Login as \n->{username}")
    return RedirectResponse(url="/", status_code=303)
    # return "Successful."