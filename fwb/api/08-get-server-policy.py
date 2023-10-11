import requests
import json
requests.packages.urllib3.disable_warnings() ##disable ssl warning

FWB_IP="172.23.132.87"
#FWB_IP="172.23.144.161"
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}cmdb/server-policy/policy?mkey-baniptest"
#FWB_FUNC_URL = FWB_URL + "cmdb/server-policy/policy?mkey=configsynctest"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json"
}
PAYLOAD={}

RESPONSE = requests.request("GET", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
print(RESPONSE.text)
J_R=json.loads(RESPONSE.text)
print(J_R)
#print(J_R["name"])

