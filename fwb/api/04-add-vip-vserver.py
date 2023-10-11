import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.85"
#FWB_IP = "172.23.132.85"
PORT = "port2"
VIP_LIST = [ '10.2.1.51', '10.2.1.52',]

FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_VIP_URL = f"{FWB_URL}cmdb/system/vip"
FWB_VSERVER_URL = f"{FWB_URL}cmdb/server-policy/vserver"
#print (FWB_VSERVER_URL)
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

# VIP_01='10.1.11.1'
# VIP_02='10.1.11.12'
# VIP_03='10.1.11.13'
# VIP_LIST = [
#     VIP_01,
#     VIP_02,
#     VIP_03,
# ]

for i in VIP_LIST:
    VIP_DATA = f'{{"data": {{"vip": "{i}/32","vip6": "::/0","name": "{PORT}-{i}","interface": "{PORT}"}}}}'
    RESPONSE = requests.request("POST", FWB_VIP_URL, headers=HEADERS, data=VIP_DATA, verify=False)
    print (RESPONSE.text)
    VSERVER_DATA = f'{{"data": {{"name": "{i}"}}}}'
    RESPONSE = requests.request("POST", FWB_VSERVER_URL, headers=HEADERS, data=VSERVER_DATA, verify=False)
    print (RESPONSE.text)
    MKEYURL = f"{FWB_VSERVER_URL}/vip-list?mkey={i}"
    MKEYDATA = f'{{"data": {{"use-interface-ip": "disable", "status": "enable", "vip": "{PORT}-{i}"}}}}'
    RESPONSE = requests.request("POST", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
    print(RESPONSE.text)
    '''
    print (VIP_DATA)
    print (VSERVER_DATA)
    print (MKEYURL)
    print (MKEYDATA)
    '''