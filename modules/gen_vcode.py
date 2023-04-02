from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

from asyncio import run

from datetime import datetime

number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

async def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=4):

    captcha_text = []

    for _ in range(captcha_size):

        c = random.choice(char_set)
        captcha_text.append(c)

    return captcha_text
 
async def gen_captcha_text_and_image():
    image = ImageCaptcha()

    captcha_text = await random_captcha_text()
    captcha_text = ''.join(captcha_text)

    captcha = image.generate(captcha_text)

    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image
 
async def genVCODE():
    dt = datetime.now().strftime("%Y%m%d %H-%M-%S")
    text, image = await gen_captcha_text_and_image()
    # f = plt.figure()
    # ax = f.add_subplot(111)
    # ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
    plt.axis("off")
    plt.imshow(image)
    plt.savefig(f"static/img/vcode.png")

    return text, image