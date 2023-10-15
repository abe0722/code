#!/usr/bin/env python3
import paramiko
import time

HOST = "172.23.144.162"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(HOST, username="admin", password="fortinet")
ssh.exec_command('config system global \n set hostname 123 \n end \n end')
stdin, stdout, stderr = ssh.exec_command('get system status')
print(stdout.readlines())

ssh.close()


# for region in range(23, 27):
#     for device in range (1, 6):
#         for port in range (1, 3):
#             nr = "%02d" % region
#             ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('esxcfg-vswitch --add-pg=tag-vlan-' +str(nr)+str(device)+str(port)+ ' vmnic2-switch');
#             time.sleep (0.2);
#             ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('esxcfg-vswitch -v ' +str(region)+str(device)+str(port)+ ' -p tag-vlan-' +str(nr)+str(device)+str(port)+ ' vmnic2-switch')
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('vim-cmd hostsvc/net/refresh');
