from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


if __name__ == '__main__':
    image_name = "download.jpg"
    try:
        img = Image.open(image_name)
    except IOError:
        pass
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Black.ttf", 16)
    text = "Hello World!"
    draw.text((0, 0),text,(255,255,255),font=font)
    img.save('sample-out.jpg')