import requests
import json
requests.packages.urllib3.disable_warnings() ##disable ssl warning

FWB_IP="172.23.132.84"
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}waf/webcache.check"
FUNC="CHECK" #CHECK or DELETE
WEB_CACHE_POLICY="Policy-10.1.11.41" #web cache policy name
CACHE_URL = "https://10.1.11.41/get"
HTTP_METHOD = "GET" #GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE
ACCEPT_ENCODING = "gzip" #br,gzip, deflate, other
COOKIE = "user=moore;id=2" #"user=abe;id=1", "user=ruojia", "id=3"

HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Content-Type":"text/plain"
  #"Content-Type":"application/json"
}
PAYLOAD={"url":CACHE_URL, "method":HTTP_METHOD, "accept-encoding":ACCEPT_ENCODING, "policy_name":WEB_CACHE_POLICY}
if COOKIE:  #if COOKIE has value
    PAYLOAD["cookie"] = COOKIE

PAYLOAD=json.dumps(PAYLOAD)
RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
R1=json.loads(RESPONSE.text)
if R1['found']==True:
    if FUNC=="CHECK":
        print(R1)
        print("KEY="+R1['key'])
    else:
        PAYLOAD = {"policy_name": WEB_CACHE_POLICY, "key": R1['key']}
        PAYLOAD = json.dumps(PAYLOAD)
        RESPONSE = requests.request("DELETE", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
        print("The KEY is deleted, Response:" + RESPONSE.text)
else:
    print("KEY not Found")