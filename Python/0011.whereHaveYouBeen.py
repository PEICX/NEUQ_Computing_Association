#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 18:25:28
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$

from winreg import *


def val2addr(val):
    addr = ""
    for ch in val:
        # x是16进制，2是二位，不够的用0填充
        addr += ("%02x" % (ch)) + ":"
        # 包括:在内，共17位，取前17位巧妙去除末尾的冒号
        addr = addr.strip(" ")[0:17]
    return addr


def printNets():
    # 该子键储存所有连接过的网络信息
    net = ("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
           "\\NetworkList\\Signatures\\Unmanaged")
    key = OpenKey(HKEY_LOCAL_MACHINE, net)
    print("\n[*] Networks You have Joined.")
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            netKey = OpenKey(key, str(guid))
            # 网络名和网关的键读取时默认储存在第四和五
            (n, addr, t) = EnumValue(netKey, 5)
            (n, name, t) = EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print('[+] ' + netName + '    ' + macAddr)
        except:
            break


if __name__ == '__main__':
    printNets()
