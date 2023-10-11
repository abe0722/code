import requests
import json
import sys
requests.packages.urllib3.disable_warnings() ##disable ssl warning

FWB_IP="172.23.132.84"
#FWB_IP="172.23.144.161"
WEB_CACHE_POLICY="Policy-10.1.11.41" #web cache policy
# print (sys.argv[1])
# WEB_CACHE_POLICY = str(sys.argv[1])

FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}waf/webcache.list"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json"}
PAYLOAD={}

###Get web cache policy list
RESPONSE = requests.request("GET", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
R1=json.loads(RESPONSE.text)
# print(R1)

###Get web cache policy id and clear the cache
LIST=R1['results']['datas']  #get all web cache policy
print (LIST)
for items in LIST:
    print(items)
    if items["policy"] == WEB_CACHE_POLICY:
        name = items["name"]
        FWB_FUNC_URL = f"{FWB_URL}waf/webcache.data?mkey={name}"
        RESPONSE = requests.request("DELETE", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
        print (RESPONSE.text)