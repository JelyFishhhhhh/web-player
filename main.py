from fastapi import FastAPI
from uvicorn import Config, Server
from aiofiles import open as aopen
from asyncio import run

from modules import Json, playList

app = FastAPI()

CONFIG = Json.load_nowait("config.json")

@app.get("/")
async def home():

    # URL = {"敦化南路":"https://www.youtube.com/watch?v=f5FN4-HN_JQ"}
    # music = playList()
    # await music.Push(name = "敦化南路", url = "https://www.youtube.com/watch?v=f5FN4-HN_JQ")

    return "Hello, World."

if __name__ == "__main__":
    
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    server.run()