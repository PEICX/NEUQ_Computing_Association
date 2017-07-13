#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-08 17:17:49
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://peicx.github.io
# @Version : $Id$

'''
不能在 windows 系统下使用，因为win下没有 spawn 函数
'''
import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(child, cmd):
    '''接收一个SSH会话和命令字符串，并把结果打印出来'''
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password, port):
    ssh_newkey = 'Are you sure want to continue connecting'
    connStr = 'ssh ' + user + '@' + host + ' -p ' + str(port)
    child = pexpect.spawn(connStr)
    # expect 正则匹配里面的内容，并返回第一匹配的index
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] Error connecting')
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = '104.194.81.199'
    user = 'root'
    password = 'password'
    port = '23665'
    child = connect(user, host, password, port)
    # 连接成功后执行一个命令，并打印出来
    send_command(child, 'w')


if __name__ == '__main__':
    main()
