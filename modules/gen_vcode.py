import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice
from io import BytesIO
from asyncio import run
from datetime import datetime

FONTS = tuple(map(lambda i : ImageFont.truetype("static/fonts/DeliciousHandrawn-Regular.ttf", size = i), range(150, 180)))

async def random_captcha_operation():

    a = randint(10, 90);b = randint(10, 90)
    
    answer = a + b

    while answer < 9 or answer > 99:

        if answer > 99:
        
            answer %= 99
            answer += randint(1, 9)
        
        else:
            
            answer += randint(1, 9)

    tmp = answer-10

    if tmp < 10:
        tmp = 10

    a = answer - randint(10, tmp)

    b = answer - a

    return f"{a}+{b}=?", answer
 
async def random_color(l_range: int = 0, r_range: int = 255):

    return tuple(map(lambda x: randint(l_range, r_range), range(3)))

async def gen_image():
    
    operation, answer = await random_captcha_operation()

    image = Image.new(mode = "RGB", 
                      size = (700, 300), 
                      color = await random_color(155)
                    )
    
    draw_image = ImageDraw.Draw(image)

    for i in range(randint(5, 7)):

        x1, x2, x3 = map(lambda x: randint(0, 700), range(3))
        y1, y2, y3 = map(lambda x: randint(0, 300), range(3))
        
        draw_image.line((x1, y1, x2, y2), 
                        fill = await random_color(), 
                        width = randint(5, 25)
                    )
        for _ in range(randint(3, 5)):
            draw_image.arc((x3, y3, x3 + randint(-512, 512), 
                            y3 + randint(-100, 100)),
                            randint(0, 360), 
                            randint(0, 360),
                            await random_color(), 
                            randint(5, 24)
                        )
            
    for idx, element in enumerate(operation):
        draw_image.text(xy=(100 * idx, randint(-24, 24)), 
                        text=element,
                        fill=await random_color(0, 140), 
                        font=choice(FONTS), 
                        stroke_width=randint(1, 3)
                    )
    
    byte = BytesIO()
    # image.save(fp = byte, format = "png")
    image.save(fp = "static/cache/vcode.png", format="png")
    return answer, byte.getvalue()
 
async def genVCODE():
    # dt = datetime.now().strftime("%Y%m%d %H-%M-%S")
    text, image = await gen_image()

    return text, image

class valid_code:
    
    def __init__(self) -> None:
        self.data = {}
        pass

    async def update(self, session: str, answer: str):

        self.data[session] = (answer, datetime.now().strftime("%Y%m%d %H-%M-%S"))

    async def auth(self, session: str, request: str):

        if session is None:
            return False
        answer = self.get(session)

        if answer is None or valid_code != answer:
            return False
        
        self.remove(session)
        return True