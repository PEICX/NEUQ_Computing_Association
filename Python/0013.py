from urllib.request import *
from bs4 import BeautifulSoup
import re
import os


def scrape(url):
    html = urlopen(url)
    obj = BeautifulSoup(html, "html.parser")
    pic = obj.findAll("cc")
    path = "new_dir"
    mk_dir(path)
    cnt = 0
    for item in pic:
        it = item.findAll("img", {"src": re.compile(r'http://imgsr')})
        for i in it:
            urlretrieve(str(i.attrs['src']), path + '/' + str(cnt) + ".jpg")
            cnt += 1


def mk_dir(_path):
    if not os.path.exists(_path):
        os.mkdir(_path)


def download():
    pass


_url = "http://tieba.baidu.com/p/2166231880"
scrape(_url)

