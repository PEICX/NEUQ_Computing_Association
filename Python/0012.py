#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-29 09:14:37
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$

from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


def get_char(r, g, b):
    if r == g == b == 255:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]



with open('test.txt', 'w') as f:
    im = Image.open('1.jpg')
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            (r, g, b) = im.load()[i, j]
            f.write(get_char(r, g, b))
        f.write(('\n'))
