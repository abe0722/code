import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP="52.195.227.81:8443"
PORT = "port1"
VIP_LIST = [ '10.2.1.71', '10.2.1.72',]

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



VSERVER_DATA = f'{{"data": {{"name": "Port1_Virtual_Server"}}}}'
RESPONSE = requests.request("POST", FWB_VSERVER_URL, headers=HEADERS, data=VSERVER_DATA, verify=False)
print (RESPONSE.text)
MKEYURL = f"{FWB_VSERVER_URL}/vip-list?mkey=Port1_Virtual_Server"
MKEYDATA = f'{{"data": {{"use-interface-ip": "enable", "status": "enable", "interface": "port1"}}}}'
RESPONSE = requests.request("POST", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
print(RESPONSE.text)
