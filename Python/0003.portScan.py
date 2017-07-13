#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-14 16:50:24
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$


import argparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    '''建立指定目标主机和端口的连接'''
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'ViolentPython\r\n')
        results = connSkt.recv(100)
        # 执行加锁操作
        screenLock.acquire()
        print('[+] %d/tcp open' % tgtPort)
        # 此处输出结果包括一些控制符，用utf-8解码时会出错
        print('[+] ' + str(results, encoding='utf-8'))
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed' % tgtPort)
    finally:
        # 释放信号量
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    '''
    首先通过主机名确定IP地址，然后用connScan尝试连接每个端口
    '''
    try:
        # 通过域名或主机名获取IP地址，Web服务器主机名有时称为域名
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve ' % s':Unknown host" % tgtHost)
        return
    try:
        # 通过IP地址得到一个三元组，
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIP)
    # 设置默认超时
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


def main():
    parser = argparse.ArgumentParser(
        description="This is a tcp port scanning.")
    parser.add_argument('-H', dest='tgtHost', type=str,
                        help='specify target host')
    parser.add_argument('-p', dest='tgtPort', type=str,
                        help='specify target port[s] separated by comma')
    options = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) or (tgtPorts[0] is None):
        print('[-] You must specify a target host and port[s].')
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
