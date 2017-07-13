#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-14 11:22:39
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$


import zipfile
import argparse
from threading import Thread


def extractFile(zFile, password):
    try:
        # extractall函数能解压文件，也能指定密码解压
        # 注意此处encoding，Python3没有此选项会报错
        zFile.extractall(pwd=bytes(password, encoding='utf-8'))
        print("[+] Password = " + password)
    except:
        pass


def main():
    # 初始化一个解析器对象，默认生成 usage
    parser = argparse.ArgumentParser(
        description="ZIP file cracker")
    # 添加参数，参数的值可以用过dest的属性去调用
    parser.add_argument('-f', dest='zname', type=str,
                        help='specify zip file')
    parser.add_argument('-d', dest='dname', type=str,
                        help='specify dictionary file')
    # 解析参数，返回一个命名空间
    # 该对象可以通过参数的dest属性去调用他的值
    options = parser.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        # 打开zip文件，并创建一个zipfile的对象
        zFile = zipfile.ZipFile(zname)
        # 打开密码字典文件
        passFile = open(dname)
        for line in passFile.readlines():
            password = line.strip('\n')
            # 用线程提高测试速度
            t = Thread(target=extractFile, args=(zFile, password))
            t.start()


if __name__ == '__main__':
    main()
