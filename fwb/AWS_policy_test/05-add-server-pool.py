import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP="52.195.227.81:8443"
#FWB_IP = "43.206.194.63:8443"
IP_LIST = [ '54.168.43.29']
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_SERVERPOOL_URL = f"{FWB_URL}cmdb/server-policy/server-pool"
HTTP_METHOD = "POST" # "GET" or "POST"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

for i in IP_LIST:
    SERVERPOOL_DATA = f'{{"data": {{"name": "{i}","type":"reverse-proxy","server-balance":"disable"}}}}'
    RESPONSE = requests.request (f"{HTTP_METHOD}", FWB_SERVERPOOL_URL, headers=HEADERS, data=SERVERPOOL_DATA, verify=False)
    print (RESPONSE.text)
    MKEYURL = f"{FWB_SERVERPOOL_URL}/pserver-list?mkey={i}"
    MKEYDATA = f'{{"data":{{"status":"enable","ip":"{i}","port":80}}}}'
    RESPONSE = requests.request("POST", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
    print(RESPONSE.text)