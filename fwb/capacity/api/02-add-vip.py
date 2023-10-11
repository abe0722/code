import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.87"
PORT = "port2"
VIP_LIST = [ '10.2.1.71', '10.2.1.72',]

FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}cmdb/system/vip"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

for i in VIP_LIST:
    VIP_DATA = f'{{"data": {{"vip": "{i}/32","vip6": "::/0","name": "{PORT}-{i}","interface": "{PORT}"}}}}'
    RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=VIP_DATA, verify=False)
    print(RESPONSE.text)

# RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=VIP_DATA_01, verify=False)
# print(RESPONSE.text)