#!/usr/bin/env python3
import paramiko
import time
import ipaddress

FWB_IP = "172.23.144.162"
CUSTOMER_PORT = [ '8080', '8443',]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(FWB_IP, username="admin", password="fortinet")
command = ssh.invoke_shell()

def add_customer_service():
    command.send('config server-policy service custom \n')
    for i in CUSTOMER_PORT:
        command.send('edit ' + str(i) + '\n')
        command.send('set port ' + str(i) + '\n')
        command.send('next \n')
        time.sleep(0.1)
        print (command.recv(65535).decode('ascii'))
    command.send('end \n')
    time.sleep(1)
    output = command.recv(65535).decode('ascii')
    print (output)
    ssh.close()

add_customer_service()