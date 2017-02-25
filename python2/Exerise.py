#coding=utf-8
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random
# 随机的字母
def random_Char():
    return chr(random.randint(65,90))
# 字母所需颜色
def random_char_Color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
# 图片底部颜色
def random_pic_Color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def make_Code_pic():
    height = 60
    width = 60*4
    image = Image.new('RGB',(width,height),(255,255,255))
    drawImage = ImageDraw.Draw(image)
    # Font = ImageFont.truetype('/Library/Fonts/Arial.tff', 36)
    Font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
    # 画噪点
    for x in range(width):
        for y in range(height):
            drawImage.point((x,y),fill = random_pic_Color())
    # 将英文字添加到图片
    for c in range(4):
        drawImage.text((60*c+10,10),random_Char(),fill=random_char_Color(),font=Font)
    # 加模糊
    image = image.filter(ImageFilter.BLUR)
    image.save('exerisecode.jpg','jpeg')

if __name__=='__main__':
    make_Code_pic()
    print 'Finished'