import requests
import json
requests.packages.urllib3.disable_warnings() ##disable ssl warning

FWB_IP="172.23.132.81"
POLICY_NAME = "Policy-10.1.11.11"
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}cmdb/server-policy/policy?mkey={POLICY_NAME}"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

#Enable web cache in policy
DATA = f'{{"data": {{"web-cache":"enable"}}}}'
RESPONSE = requests.request ("PUT", FWB_FUNC_URL, headers=HEADERS, data=DATA, verify=False)
print(RESPONSE.text)

#Get Policy id
PAYLOAD = {}
RESPONSE = requests.request("GET", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
# print(RESPONSE.text)
# print (type(RESPONSE.text))
R1=json.loads(RESPONSE.text)
PID=R1['results']['policy-id']
print(PID)
# print(type(R2))
# P_ID=R2['policy-id']
# print (P_ID)
# print (type(J_NAME))

