import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.87"

FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNC_URL = f"{FWB_URL}system/maintenance.restoreconfiguration"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  #"Accept":"application/json",
  "Content-Type":"text/plain"
}

PAYLOAD={"encryption":1, "password":123456, "file":"C:/Users/atseng/Desktop/1234_20230524223036_system.conf.zip"}
RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=PAYLOAD, verify=False)
print(RESPONSE.text)

# RESPONSE = requests.request("POST", FWB_FUNC_URL, headers=HEADERS, data=VIP_DATA_01, verify=False)
# print(RESPONSE.text)