from router import app
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import Config, Server
from aiofiles import open as aopen
from asyncio import run, new_event_loop
from os.path import isfile

from gen_config import *
from modules import Json, playList
from modules.user import ENGINE, method

@app.get("/check/{page}")
async def templates(page):
    
    files = f"templates/{page}.html"

    if isfile(files):

        async with aopen(files, mode="rb") as html_file:

            return HTMLResponse(await html_file.read())
    
    else:
        return "404 Not-Found"

@app.get("/JelyFishhhhhh")
async def EASTER_EGG():
    return "Hello, Inspector :)"

if __name__ == "__main__":
    
    with open (".private", "r+") as privacy_file:
        for f in privacy_file:
            f = f[:-2]
            if not isfile(f):
                
                _ = open(f, "w+")
                
                if f == "config.json":
                
                    gen_CONFIG()

    
    CONFIG = Json.load_nowait("config.json")
    run(method.sql_init(debug=CONFIG["DEBUG"]))
    
    app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    
    loop = new_event_loop()
    app_tasks = loop.create_task(server.serve())
    loop.run_until_complete(app_tasks)
    loop.stop()

    # for task in all_tasks(loop=loop):
    #     task.cancel()

# URL = {"敦化南路":"https://www.youtube.com/watch?v=f5FN4-HN_JQ"}
# music = playList()
# await music.Push(name = "敦化南路", url = "https://www.youtube.com/watch?v=f5FN4-HN_JQ")
