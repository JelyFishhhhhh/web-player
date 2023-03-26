from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import Config, Server
from aiofiles import open as aopen
from asyncio import run
from os.path import isfile
import sqlite3 as sql

from gen_config import *
from modules import Json, playList

app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
CONFIG = Json.load_nowait("config.json")
connection = sql.connect("user.db")

# config檔製作
if not isfile("config.json"):
    f = open("config.json", "w+")
    run(gen_CONFIG())

if not isfile("user.db"):
    f = open("user.db", "w+")

@app.get("/login")
async def login():

    async with aopen ("templates/login.html", "rb") as html_file:
    
        return HTMLResponse(await html_file.read())


@app.get("/")
async def home():
    async with aopen ("templates/index.html", mode="rb") as html_file:

        return HTMLResponse(await html_file.read())
    
@app.get("/check/{page}")
async def templates(page):
    
    files = f"templates/{page}.html"

    if isfile(files):

        async with aopen(files, mode="rb") as html_file:

            return HTMLResponse(await html_file.read())
    
    else:
        return "404 Not-Found"

@app.post("/login")
async def login(username:str  = Form(...), password:str = Form(...)):

    # print(f"Received login request with username={username} and password={password}")
    return RedirectResponse(url="/", status_code=303)
    # return "Successful."

@app.get("/JelyFishhhhhh")
async def EASTER_EGG():
    return "Hello, Inspector :)"

@app.exception_handler(404)
async def NOTFOUND(requests, exc):
    
    return "404 Not-Found"

@app.exception_handler(500)
async def INTERNAL_ERR0R(requests, exc):
    
    return "waiting for developers found this bug :("

if __name__ == "__main__":
    
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    server.run()

# URL = {"敦化南路":"https://www.youtube.com/watch?v=f5FN4-HN_JQ"}
# music = playList()
# await music.Push(name = "敦化南路", url = "https://www.youtube.com/watch?v=f5FN4-HN_JQ")
