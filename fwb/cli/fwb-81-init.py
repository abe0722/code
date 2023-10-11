from netmiko import Netmiko

fw_01 = {'host': '172.23.132.85',
         'username':'admin',
         'password':'fortinet',
         'device_type':'fortinet'
}

print(f"{'#'*20} Connecting to the Device {'#'*20}")
net_connect = Netmiko(**fw_01)
#print(net_connect.find_prompt())
#command = 'show full-configuration'
#full_config = net_connect.send_command(command)
#print(full_config)
config = [
'config system interface',
  'edit port1',
    'set ip 10.1.11.81/24',
    'end',
'config system global',
  'set admintimeout 480',
  'set timezone 60',
  'end',
'config system global',
  'set shell-access enable',
  'set shell-timeout 1200',
  'set shell-username shell',
  'set shell-password fortinet',
  'end',
'config system vip',
  'edit port1-10.1.11.11',
    'set vip 10.1.11.11/32',
    'set interface port1',
  'next',
'end'
]
send_config = net_connect.send_config_set(config)
print(send_config)
#print(f"{'#'*20} Connected {'#'*20}")
