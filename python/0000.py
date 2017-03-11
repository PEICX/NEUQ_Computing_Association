from PIL import Image, ImageDraw, ImageFont

try:
    im = Image.open('a.jpg')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 100)  # truetype 为全真字体，格式为ttf
    draw.text((im.size[0]-120, 0), "99", fill=(255, 0, 0), font=font)  # fill参数可以用RGB颜色模式
    im.save("test.jpg", "jpeg")  # 保存的格式为jpg，但是在参数里必须写jpeg
except IOError:                 # 读取文件失败返回这个错误
    print("读取失败")
