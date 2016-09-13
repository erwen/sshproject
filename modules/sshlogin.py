#!/usr/bin/env python
import pexpect

class sshCmd:

    def login(self, serverDict, username, password):
        hostname = serverDict.get('hostname')
        ip = serverDict.get('ip')
        port = serverDict.get('port')
        cmd = '/usr/bin/ssh ' + ip + ' -p' + ' ' + port + ' -l ' + username
        p = pexpect.spawn(cmd)
        p.expect("assword:")
        p.sendline(password)
        p.interact()
