#!/usr/bin/env python
import paramiko

class sshcmd:
    def __init__(self, serverList, user, password, command, output=True):
        self.serverList = serverList
        self.user = user
        self.password = password
        self.command = command
        self.output = output

    def runCmd(self, hostname, port, ip, user, command, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, self.user, self.password)
        stdin, stdout, stderr = ssh.exec_command(self.command)
        if self.output == True:
            outPut = stdout.readlines()
            errPut = stderr.readlines()
            print(hostname)
            print('_________________________Begin______________________________________')
            print(''.join(outPut))
            print(''.join(errPut))
            print('..........................End.......................................')
        ssh.close()

    def main(self):
        for i in self.serverList:
            port = int(i.get('port'))
            ip = i.get('ip')
            hostname = i.get('hostname')
            self.runCmd(hostname, port, ip, self.user, self.command, self.password)
