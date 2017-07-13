#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-07 20:49:34
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$

'''
用nmap模块写的端口扫描，语法简单，功能强大，但是比较耗时
用这个模块时，依赖本地安装nmap软件
'''
import nmap
import argparse


def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print("[*] " + tgtHost + " tcp/" + tgtPort + " " + state)


def main():
    parser = argparse.ArgumentParser(description="nmapScan")
    parser.add_argument('-H', dest='tgtHost', type=str,
                        help='specify target host')
    parser.add_argument('-p', dest='tgtPort', type=str,
                        help='specify target port[s] separated by comma')
    options = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost is None) or (tgtPorts[0] is None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
