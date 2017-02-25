#coding=utf-8
# 0010 使用python生成类似于下图中的字母验证码图片
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
def randomChar():
    return chr(random.randint(65,90))
def randomColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def randomColor2():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

width = 60*4
height = 60
image = Image.new('RGB',(width,height),(255,255,255))
font = ImageFont.truetype('/Library/Fonts/Arial.ttf',36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=randomColor1())
for t in range(4):
    draw.text((60*t+10,10),randomChar(),font=font,fill=randomColor2())
image = image.filter(ImageFilter.BLUR)
image.save('code{}.jpg'.format(randomChar()),'jpeg')
