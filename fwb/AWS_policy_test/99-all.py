import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "184.72.75.68:8443"
#FWB_IP = "172.23.132.85"
SERVER_POOL = "54.168.43.29"
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
PORT = "port1"

HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

###Add VIP Server
def add_vip_server():
    #VIP_LIST = [ '10.2.1.71', '10.2.1.72',]
    FWB_VIP_URL = f"{FWB_URL}cmdb/system/vip"
    FWB_VSERVER_URL = f"{FWB_URL}cmdb/server-policy/vserver"
    VSERVER_DATA = f'{{"data": {{"name": "{PORT}_Virtual_Server"}}}}'
    RESPONSE = requests.request("POST", FWB_VSERVER_URL, headers=HEADERS, data=VSERVER_DATA, verify=False)
    print (RESPONSE.text)
    MKEYURL = f"{FWB_VSERVER_URL}/vip-list?mkey={PORT}_Virtual_Server"
    MKEYDATA = f'{{"data": {{"use-interface-ip": "enable", "status": "enable", "interface": "{PORT}"}}}}'
    RESPONSE = requests.request("POST", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
    print(RESPONSE.text)

###Add Server Pool
def add_server_pool():
    IP_LIST = [ SERVER_POOL ]
    FWB_SERVERPOOL_URL = f"{FWB_URL}cmdb/server-policy/server-pool"
    HTTP_METHOD = "POST" # "GET" or "POST"
    for i in IP_LIST:
        SERVERPOOL_DATA = f'{{"data": {{"name": "{i}","type":"reverse-proxy","server-balance":"disable"}}}}'
        RESPONSE = requests.request (f"{HTTP_METHOD}", FWB_SERVERPOOL_URL, headers=HEADERS, data=SERVERPOOL_DATA, verify=False)
        print (RESPONSE.text)
        MKEYURL = f"{FWB_SERVERPOOL_URL}/pserver-list?mkey={i}"
        MKEYDATA = f'{{"data":{{"status":"enable","ip":"{i}","port":80}}}}'
        RESPONSE = requests.request("POST", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
        print(RESPONSE.text)

###Add Server policy
def add_server_policy():
    FWB_FUNCTION_URL = f"{FWB_URL}cmdb/server-policy/policy"
    SERVERPOLICY_DATA = f'{{"data": {{"name": "Policy-{PORT}","vserver":"{PORT}_Virtual_Server","server-pool":"{SERVER_POOL}","service":"HTTP","https-service":"HTTPS"}}}}'
    RESPONSE = requests.request ("POST", FWB_FUNCTION_URL, headers=HEADERS, data=SERVERPOLICY_DATA, verify=False)
    print (RESPONSE.text)

add_vip_server()
add_server_pool()
add_server_policy()


