import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

#FWB_IP="172.23.132.82"
FWB_IP="172.23.132.85"
FWB_URL="https://" + FWB_IP + "/api/v2.0/"
FWB_FUNC_URL = FWB_URL + "system/status.systemstatus"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json"
}
PAYLOAD={}

RESPONSE = requests.request("GET", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
print(RESPONSE.text)