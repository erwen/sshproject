#!/usr/bin/env python
import paramiko
import os
import sys
class copy:
    def __init__(self, localFile, remoteFile, serversList, username, password):
        self.localFile = localFile
        self.remoteFile = remoteFile
        self.serversList = serversList
        self.username = username
        self.password = password

        if not os.path.exists(self.localFile):
            print(self.localFile + ' is not exists')
            sys.exit(31)


    def copyFile(self, host, port):
        t = paramiko.Transport(host, port)
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(self.localFile, self.remoteFile)
        sftp.close()

    def main(self):
        for i in self.serversList:
            hostname = i.get('hostname')
            port = int(i.get('port'))
            ip = i.get('ip')
            self.copyFile(ip, port)
