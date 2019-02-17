from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFile
ImageFile.LOAD_TRUNCTATED_IMAGES=True

import os
import requests
from photourl import get_urls
from prawdata import get_subreddit_titles
import random

def pick_url():
    return random.choice(get_urls())

def pick_title():
    return random.choice(get_subreddit_titles("dogshowerthoughts"))


def show_meme():
    with open('pic1.jpg', 'wb') as handle:
        response = requests.get(pick_url(), stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

        image_name = "pic1.jpg"

        try:
            img = Image.open(image_name)
        except IOError:
            print("IOError")
            pass

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Roboto-Black.ttf", 100)
        text = pick_title()
        draw.text((0, 0),text,(255,255,255),font=font)
        img.show()


show_meme()