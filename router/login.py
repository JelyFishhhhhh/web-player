from typing import Optional
from fastapi import APIRouter, Form, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from aiofiles import open as aopen
from modules import genVCODE, method, User_Profile, valid_code, gen_session_id

router = APIRouter(tags=["user"])

@router.get("/login")
async def login(session: Optional[str] = Cookie(None)):
    
    # global answer

    answer, code = await genVCODE()
    

    response = Response(content=code, headers={
                        "Cache-Control": "no-store"}, media_type="image/jpeg")
    if session is None:
        session = gen_session_id()
        response.set_cookie("session", session)
    
    valid_code.update(session, answer)
    return response

    # async with aopen ("templates/login.html", "rb") as html_file:
        
    #     return HTMLResponse(await html_file.read())
    
@router.post("/login")
async def login(username:str  = Form(...), password:str = Form(...), vcode: int = Form(...)):

    user = await method.sql_where_by_NAME(User_Profile, name=username)
    
    if await valid_code.auth(session=gen_session_id(), request=vcode):
        return {"Message": "Valid Code error"}

    elif user is None:
        return {"Message" : {"user not founded"}}
    
    elif user.password != password:
        return {"Message" : {"password error"}}
    
    else:
        print(f">>>Login as \n->{username}")
        return RedirectResponse(url="/", status_code=303)
