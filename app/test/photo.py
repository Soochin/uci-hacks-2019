from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import requests
import test


if __name__ == '__main__':
    #image_name = "download.jpg"

    #urllib.urlretrieve("https://i.redd.it/s9rva3317xg21.jpg", "00000001.jpg")

    # f = open('00000001.jpg', 'wb')
    # f.write(urllib.request.urlopen('https://i.redd.it/s9rva3317xg21.jpg').read())
    # f.close()

    # image_url = "https://i.redd.it/s9rva3317xg21.jpg"
    # img_data = requests.get(image_url).content
    # with open('image_name.jpg', 'wb') as handler:
    #     handler.write(img_data)

    pic_url = "https://i.redd.it/6d4zw22o40h21.jpg"



    with open('pic1.jpg', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print (response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    image_name = "pic1.jpg"

    try:
        img = Image.open(image_name)
    except IOError:
        pass
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Black.ttf", 100)
    text = "Hello World!"
    draw.text((0, 0),text,(255,255,255),font=font)
    img.show()
    # img.save('sample-out.jpg')
