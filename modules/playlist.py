# from playsound import playsound
from typing import Any, Optional, Union
from .json import Json
from orjson import OPT_INDENT_2
from aiofiles import open as aopen
from os.path import isdir
from os import mkdir
from orjson import dumps

# print("Hello")
class playList:
    
    @staticmethod
    async def Push(
        name : str, 
        url: str
    ) -> None:
        
        # info = dict(name, url)
        info = {}
        info[name] = url
        async with aopen(f"queue.json", mode = "wb") as __file:
            await __file.write(dumps(info, option=OPT_INDENT_2))

        print(f"Push >>> {url}")
        return
    
