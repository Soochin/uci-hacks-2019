# client_id = "107675bc7016b8b"
# client_secret = "8541e4d2428e8b8444285e1a33fc935bd0219559"
#
# base_url = "https://api.imgur.com/3/"
#
# require: {
#     "boris/imgscrape": "0.*"
# }


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


if __name__ == '__main__':
    try:
        img = Image.open("download.jpg")
    except IOError:
        pass
    #img.show()
    draw = ImageDraw.Draw(img)
    # # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("Roboto-Black.ttf", 16)
    #draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    img.save('sample-out.jpg')