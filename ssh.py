#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect


def ssh_detect(ip, passwd):
    try:
        ssh_ex = pexpect.spawn('ssh root@' + ip)
        ssh_ex.expect('root@' + ip + '\'s password:', timeout=1)
        ssh_ex.sendline(passwd)
        ssh_ex.expect('Last login:', timeout=1)
        return True
    except:
        return False
print ssh_detect('123.12.21.2', 'EQW')
