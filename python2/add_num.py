#coding = utf-8
from PIL import Image, ImageDraw, ImageFont
def add_num_to_img(im,sign="42"):
    width,height = im.size
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf',min(width//6,height//6))
    draw.text((width*0.75,height*0.075),sign,font=font,fill=(255,33,33,255))
    im.save('result.jpg','jpeg')

if __name__=='__main__':
    image = Image.open('sample.jpg')
    add_num_to_img(image)
    print 'Finished'


