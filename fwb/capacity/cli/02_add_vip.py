#!/usr/bin/env python3
import paramiko
import time
import ipaddress

HOST = "54.95.249.239"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username="admin", password="fortinet")
command = ssh.invoke_shell()

def add_vip():
    command.send('config system vip \n')
    for i in range(1, 501):
        n1 = ipaddress.ip_address('1.1.1.0')+i
        command.send('edit ' + str(n1) + '\n')
        command.send('set vip ' + str(n1) + '/32 \n')
        command.send('set interface port1 \n')
        command.send('next \n')
        time.sleep(0.1)
        print (command.recv(65535).decode('ascii'))
    command.send('end \n')
    time.sleep(3)
    output = command.recv(65535).decode('ascii')
    print (output)
    ssh.close()

add_vip()




# for region in range(23, 27):
#     for device in range (1, 6):
#         for port in range (1, 3):
#             nr = "%02d" % region
#             ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('esxcfg-vswitch --add-pg=tag-vlan-' +str(nr)+str(device)+str(port)+ ' vmnic2-switch');
#             time.sleep (0.2);
#             ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('esxcfg-vswitch -v ' +str(region)+str(device)+str(port)+ ' -p tag-vlan-' +str(nr)+str(device)+str(port)+ ' vmnic2-switch')
# ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('vim-cmd hostsvc/net/refresh');
