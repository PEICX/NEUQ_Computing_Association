#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-14 16:50:24
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://github.com/peicx
# @Version : $Id$

import argparse
from pexpect import pxssh


class Client():
    """docstring for Client"""

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        try:
            self.session.sendline(cmd)
            self.session.prompt()
            return str(self.session.before, encoding='utf-8')
        except Exception as e:
            pass


def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)


def botnetCommand(cmd):
    for client in botNet:
        output = client.send_command(cmd)
        print('[*] output from ' + client.host)
        print('[+] ' + output + '\n')

    return client.before

botNet = []


addClient('10.10.10.129', 'root', 'root')


botnetCommand('uname -v')
