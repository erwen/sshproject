#!/usr/bin/env python
import sys
class Config:
    def __init__(self, file):
        self.file = file

    def getData(self):
        TypeList=[]
        configDir={}

        try:
            f = open(self.file, 'r')
        except IOError:
            print('No config file')
            sys.exit()
        n=0
        while not n:
            line = f.readline()
            if len(line) == 0:
                n = 1
            if line.startswith('['):
                serverType = line.strip('[').strip(']\n')
                TypeList.append(serverType)
                serverList = []
            if line.startswith('srv'):
                hostname = line.split()[0]
                ip = line.split()[1]
                port = line.split()[2]
                serverDir = {}
                serverDir['hostname'] = hostname
                serverDir['ip'] = ip
                serverDir['port'] = port
                serverList.append(serverDir)
                configDir[serverType]=serverList

            configDir['server_type']=TypeList

        return  configDir

#Get type and server info dict
    def getType(self):
        typeDataDict = self.getData()
        # del dataDict['customername']
        del typeDataDict['server_type']
        return typeDataDict

#Get type list
    def getTypeList(self):
        typeList=[]
        dataDict = self.getType()
        for i in dataDict:
            typeList.append(i)
        return typeList

#Get all servers info list
    def getServersInfo(self):
        serversInfoList=[]
        dataDict = self.getType()
        for i in dataDict:
            serversInfoList.extend(dataDict[i])
        return serversInfoList

#Get type and servers's hostname info dict
    def getServers(self):
        typeList = self.getTypeList()
        typeDataDict = self.getType()
        serverList = []
        serverinfo = {}
        for i in typeList:
            serverList = []
            for h in  typeDataDict.get(i):
                serverList.append(h.get('hostname'))
            serverinfo[i] = serverList
        return serverinfo

#Get all hostname List
    def getServersList(self):
        serverDir = self.getServers()
        serverList = []
        for i in serverDir:
            serverList.extend(serverDir[i])
        return serverList

#Get one server info
    def getServerInfo(self, hostname):
        typeDataDict = self.getType()
        serverDict = {}
        for i in typeDataDict:
            for h in typeDataDict[i]:
                if h.get('hostname') == hostname:
                    serverDict['hostname'] = hostname
                    serverDict['ip'] = h.get('ip')
                    serverDict['port'] = h.get('port')
        return serverDict

#Get one type server hostname
    def getTypeservers(self, name):
        dataDict = self.getType()
        serverList = []
        for i in dataDict[name]:
            serverList.append(i['hostname'])
        return serverList

if __name__=='__main__':
    c = Config('../service.cf')
#     print(c.getTypeList())
#     print(c.getServers())
#     print(c.getServerInfo('srv-pv-prod-nat1'))
#    print(c.getTypeservers('nat'))
    print(c.getServersList())
