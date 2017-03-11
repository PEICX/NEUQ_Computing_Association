from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import randint


def random_color1():
    return tuple((randint(64, 256), randint(64, 256), randint(64, 256)))


def random_color2():
    return tuple((randint(32, 127), randint(32,127), randint(32,127)))


def random_char():
    return chr(randint(65, 91))


if __name__ == "__main__":
    # 画布大小为tuple元组
    size = (240, 60)
    # 创建背景为白色的画布
    im = Image.new("RGB", size, (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.Draw(im)
    # 用随机颜色填充整个画布每一个像素点，制造浑浊的背景
    for i in range(size[0]):
        for j in range(size[1]):
            draw.point((i, j), fill=random_color1())
    for k in range(4):
        draw.text((60*k + 10, 10), random_char(), font=font, fill=random_color2())
    # BLUR是变模糊的意思
    im = im.filter(ImageFilter.BLUR)
    im.show()

