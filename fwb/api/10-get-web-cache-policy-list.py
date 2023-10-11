import requests
import json
requests.packages.urllib3.disable_warnings() ##disable ssl warning

FWB_IP="172.23.132.84"
#FWB_IP="172.23.144.161"
WEB_CACHE_POLICY="Policy-10.1.11.42" #web cache policy
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}waf/webcache.list"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json"
}
PAYLOAD={}

RESPONSE = requests.request("GET", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
print(RESPONSE.text)
R1=json.loads(RESPONSE.text)


