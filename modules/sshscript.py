#!/usr/bin/env python
from .sshcopy import copy
from .sshcmd import sshcmd
def runScript(localFile, serversList, username, password):
    try:
        remoteFile = localFile.split('/')[1]
    except:
        remoteFile = localFile
    c = copy(localFile, remoteFile, serversList, username, password)
    c.main()
    command = 'chmod a+x ' + remoteFile + ';./' + remoteFile
    s = sshcmd(serversList, username, password, command)
    s.main()
    command = 'rm -f ' + remoteFile
    s = sshcmd(serversList, username, password, command, False)
    s.main()

