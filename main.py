from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from uvicorn import Config, Server
from aiofiles import open as aopen
from asyncio import run
from os.path import isfile, join, split, splitext

from modules import Json, playList

app = FastAPI()

CONFIG = Json.load_nowait("config.json")

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
    
    return "500 Internal-Server-Err0r"

if __name__ == "__main__":
    
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    server.run()

    # URL = {"敦化南路":"https://www.youtube.com/watch?v=f5FN4-HN_JQ"}
    # music = playList()
    # await music.Push(name = "敦化南路", url = "https://www.youtube.com/watch?v=f5FN4-HN_JQ")