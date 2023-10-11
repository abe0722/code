import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.82"
PORT = "port2"
VIP_LIST = [ 'ggg', 'vvv',]

FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}cmdb/server-policy/pattern.custom-data-type"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

VIP_DATA = '{"data": {"name": "yyyuyy","expression": "(^1300\\d{6}$)|(^1800|1900|1902\\d{6}$)|(^0[2|3|7|8]{1}[0-9]{8}$)|(^04\\d{2,3}\\d{6}$)"}}'
RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=VIP_DATA, verify=False)
print(RESPONSE.text)

# RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=VIP_DATA_01, verify=False)
# print(RESPONSE.text)