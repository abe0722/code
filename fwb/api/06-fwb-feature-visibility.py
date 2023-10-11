import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.84"
#FWB_IP = "172.23.144.161"
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FEATURE_VISIBILITY_URL = f"{FWB_URL}cmdb/system/feature-visibility"
FEATURE = "web-cache"
HTTP_METHOD = "PUT"  #"GET","POST","PUT"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

DATA = f'{{"data":{{"{FEATURE}":"enable"}}}}'
RESPONSE = requests.request ("PUT", FWB_FEATURE_VISIBILITY_URL, headers=HEADERS, data=DATA, verify=False)
print (RESPONSE.text)

'''
{"data":{"ftp-security":"disable","ftp-security_val":"0","traffic-mirror":"disable","traffic-mirror_val":"0",
"mobile-app-identification":"disable","mobile-app-identification_val":"0","adfs-policy":"disable","adfs-policy_val":"0",
"acceleration-policy":"disable","acceleration-policy_val":"0","web-cache":"enable","web-cache_val":"0",
"support-ajax-requests":"disable","support-ajax-requests_val":"0","wccp-mode":"disable","wccp-mode_val":"0",
"wvs":"disable","wvs_val":"0","api-gateway":"disable","api-gateway_val":"0","firewall":"disable",
"firewall_val":"0","padding-oracle":"disable","padding-oracle_val":"0","wad":"disable","wad_val":"0",
"fortigate-integration":"disable","fortigate-integration_val":"0","support-icap-server":"disable",
"support-icap-server_val":"0","debug-log":"disable","debug-log_val":"0","recaptcha":"disable","recaptcha_val":"0"}}
'''