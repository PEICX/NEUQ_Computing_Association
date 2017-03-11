from PIL import Image, ImageDraw, ImageFont


def add_num(im):
    draw = ImageDraw.Draw(im)
    # truetype 为全真字体，格式为ttf
    font = ImageFont.truetype("arial.ttf", 100)
    # fill参数可以用RGB颜色模式
    draw.text((im.size[0]-120, 0), "99", fill=(255, 0, 0), font=font)
    # 保存的格式为jpg，但是在参数里必须写jpeg
    im.save("test.jpg", "jpeg")


if __name__ == '__main__':
    im = Image.open('a.jpg')
    add_num(im)
