#!/usr/bin/env python
from modules import configsort, sshlogin, sshcmd, sshcopy, sshscript
import sys, os
import getpass

def checkArgv():
    argList=['ssh', 'cmd', 'script', 'copy', 'config']
    if len(sys.argv) == 1 or len(sys.argv) > 2 or sys.argv[1] not in argList:
        print('help')
        sys.exit(11)
    else:
        arg = sys.argv[1]
        return arg

#create configfile
def Config():
    try:
        f = open('.sshconfig', 'w')
    except IOError:
        print('Can not create config file')
        sys.exit(12)
    name = input('username:')
    password = getpass.getpass('Input you password:')
    line = 'username=' + name + '\n' +  'password=' + password
    f.write(line)
    f.close()
    sys.exit(0)

def Auth():
    if not os.path.exists('.sshconfig'):
        print('please run main.py config first')
        sys.exit(13)
    try:
        f = open('.sshconfig', 'r')
    except IOError:
        print('Can not read config file')
        sys.exit(14)
    authDict={}
    for i in f.readlines():
        list = i.split('=')
        if list[0] == 'username':
            authDict['username'] = list[1].strip()
        elif list[0] == 'password':
            authDict['password'] = list[1].strip()
    return authDict

def getList(typeName):
    if typeName in c.getTypeList():
        List = c.getType().get(typeName)
    elif typeName == 'all':
        List = c.getServersInfo()
    elif typeName in c.getServersList():
        List=[]
        Dict = c.getServerInfo(typeName)
        List.append(Dict)
    else:
        print('error')
        sys.exit(15)
    return List

def showInfo():
    #Show server list in the screen
    typeInfoList = c.getServers()
    for i in typeInfoList:
        print('[' + i + ']')
        for h in typeInfoList[i]:
            print(h)

def ssh(hostname, username, password):
    #Login the server
    serverDict = c.getServerInfo(hostname)
    s = sshlogin.sshCmd()
    s.login(serverDict, username, password)

def cmd(ServerList, username, password, command):
    cmd = sshcmd.sshcmd(ServerList, username, password, command)
    cmd.main()

def copy(localFIle, remoteFIle, serverList, username, password):
    c = sshcopy.copy(localFIle, remoteFIle, serverList, username, password)
    c.main()

if __name__=='__main__':
    arg = checkArgv()
    c = configsort.Config('service.cf')
    authDict = Auth()
    username = authDict['username']
    password = authDict['password']

    if arg == 'config':
        Config()

    authDict = Auth()
    showInfo()

    if arg == 'ssh':
        serverName = input('ServerName:')
        ssh(serverName, username, password)

    elif arg == 'config':
        Config()

    elif arg == 'cmd':
        serverInfo = input('Serve name or type:')
        command = ''
        while command != 'exit':
            command = input('Command:')
            ServerList = getList(serverInfo)
            cmd(ServerList, username, password, command)

    elif arg == 'copy':
        serverInfo = input('Serve name or type:')
        ServerList = getList(serverInfo)
        LocalFile = input('Local file:')
        RemoteFile = input('Remote file:')
        copy(LocalFile, RemoteFile, ServerList, username, password)

    elif arg == 'script':
        serverInfo = input('Serve name or type:')
        ServerList = getList(serverInfo)
        scriptLocation = input('Script Location:')
        sshscript.runScript(scriptLocation, ServerList, username, password)
