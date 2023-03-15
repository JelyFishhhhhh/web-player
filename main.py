from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import Config, Server
from aiofiles import open as aopen
from asyncio import run
from os.path import isfile, join, split, splitext

from gen_config import *

from modules import Json, playList

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

CONFIG = Json.load_nowait("config.json")

# config檔製作
if not isfile("config.json"):
    run(gen_CONFIG())

@app.get("/")
async def home():

    path = ".\\templates\\index.html"
    
    if isfile(path):

        async with aopen(path, mode="rb") as html_file:

            return HTMLResponse(await html_file.read())
    
    else:
        return "404 Not-Found"
    
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