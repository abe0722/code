#!/usr/bin/env python3
import paramiko
import time
import ipaddress

FWB_IP = "172.23.144.162"
PORT = "port2"
VIP_LIST = [ '10.2.1.21', '10.2.1.22',]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(FWB_IP, username="admin", password="fortinet")
command = ssh.invoke_shell()

def add_vip():
    command.send('config system vip \n')
    for i in VIP_LIST:
        command.send('edit ' + str(i) + '\n')
        command.send('set vip ' + str(i) + '/32 \n')
        command.send('set interface ' + PORT + '\n')
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
