import requests
requests.packages.urllib3.disable_warnings() #disable ssl warning

FWB_IP = "172.23.132.85"
VIP_LIST = [ '10.2.1.51', '10.2.1.52',]
FWB_URL = f"https://{FWB_IP}/api/v2.0/"
FWB_FUNCTION_URL = f"{FWB_URL}cmdb/server-policy/policy"
HTTP_METHOD = "POST"  #"GET","POST","PUT"
HEADERS = {
  "Authorization":"eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJmb3J0aW5ldCIsInZkb20iOiJyb290In0K",
  "Accept":"application/json",
  "Content-Type":"text/plain"
}

#Create Server Policy
# DATA1 = '{"data":{"name":"Policy-10.1.11.11","vserver":"10.1.11.11","server-pool":"10.1.11.111","service":"HTTP","https-service":"HTTPS"}}'
# RESPONSE = requests.request (f"{HTTP_METHOD}", FWB_FUNCTION_URL, headers=HEADERS, data=DATA1, verify=False)
# DATA2 = '{"data":{"name":"Policy-10.1.11.12","vserver":"10.1.11.12","server-pool":"10.1.11.111","service":"HTTP","https-service":"HTTPS"}}'
# RESPONSE = requests.request (f"{HTTP_METHOD}", FWB_FUNCTION_URL, headers=HEADERS, data=DATA2, verify=False)
# DATA3 = '{"data":{"name":"Policy-10.1.11.13","vserver":"10.1.11.13","server-pool":"10.1.11.111","service":"HTTP","https-service":"HTTPS"}}'
# RESPONSE = requests.request (f"{HTTP_METHOD}", FWB_FUNCTION_URL, headers=HEADERS, data=DATA3, verify=False)
# print (RESPONSE.text)

#Add Server Policy and enable function
# DATA1 = '{"data":{"name":"Policy-10.1.11.21","vserver":"10.1.11.21","server-pool":"10.1.11.72","service":"HTTP","https-service":"HTTPS"}}'
# URL = f"{FWB_FUNCTION_URL}?mkey=Policy-10.1.11.21"
# RESPONSE = requests.request ("POST", FWB_FUNCTION_URL, headers=HEADERS, data=DATA1, verify=False)
# print (RESPONSE.text)

for i in VIP_LIST:
    SERVERPOLICY_DATA = f'{{"data": {{"name": "Policy-{i}","vserver":"{i}","server-pool":"10.2.0.72","service":"HTTP","https-service":"HTTPS"}}}}'
    RESPONSE = requests.request ("POST", FWB_FUNCTION_URL, headers=HEADERS, data=SERVERPOLICY_DATA, verify=False)
    print (RESPONSE.text)
    # MKEYURL = f"{FWB_FUNCTION_URL}?mkey=Policy-{i}"
    # MKEYDATA = f'{{"data": {{"web-cache":"enable"}}}}'
    # RESPONSE = requests.request ("PUT", MKEYURL, headers=HEADERS, data=MKEYDATA, verify=False)
    # print(RESPONSE.text)


'''
{"data":{"protocol":"HTTP","name":"Policy-10.1.11.11","deployment-mode":"server-pool","client-real-ip":"disable",
"ssl":"enable","http2":"disable","certificate-type":"disable","multi-certificate":"disable","http-to-https":"disable",
"traffic-mirror":"disable","traffic-mirror-type":"client-side","monitor-mode":"disable","syncookie":"disable",
"half-open-threshold":8192,"case-sensitive":"disable","proxy-protocol":"disable","retry-on":"disable",
"retry-on-cache-size":512,"retry-on-connect-failure":"disable","retry-times-on-connect-failure":3,
"retry-on-http-layer":"disable","retry-times-on-http-layer":3,"retry-on-http-response-codes":"404 408 500 501 502 503 504",
"web-cache":"disable","prefer-current-session":"disable","tlog":"disable","tls-v10":"enable","tls-v11":"enable",
"tls-v12":"enable","tls-v13":"disable","ssl-cipher":"medium",
"ssl-custom-cipher":"ECDHE-ECDSA-AES256-GCM-SHA384 ECDHE-RSA-AES256-GCM-SHA384 ECDHE-ECDSA-CHACHA20-POLY1305 ECDHE-RSA-CHACHA20-POLY1305 ECDHE-ECDSA-AES128-GCM-SHA256 ECDHE-RSA-AES128-GCM-SHA256 ECDHE-ECDSA-AES256-SHA384 ECDHE-RSA-AES256-SHA384 ECDHE-ECDSA-AES128-SHA256 ECDHE-RSA-AES128-SHA256 ECDHE-ECDSA-AES256-SHA ECDHE-RSA-AES256-SHA ECDHE-ECDSA-AES128-SHA ECDHE-RSA-AES128-SHA AES256-GCM-SHA384 AES128-GCM-SHA256 AES256-SHA256 AES128-SHA256",
"http2-custom-cipher":"ECDHE-ECDSA-AES256-GCM-SHA384 DHE-DSS-AES128-GCM-SHA256 DHE-RSA-AES128-GCM-SHA256 ECDHE-RSA-AES256-GCM-SHA384",
"tls13-custom-cipher":"TLS_AES_256_GCM_SHA384","ssl-noreg":"enable","sni":"disable","sni-strict":"disable","urlcert":"disable",
"urlcert-hlen":32,"client-certificate-forwarding":"disable","client-certificate-forwarding-sub-header":"X-Client-DN",
"client-certificate-forwarding-cert-header":"X-Client-Cert","hsts-header":"disable","hsts-max-age":15552000,
"hsts-include-subdomains":"disable","hsts-preload":"disable","vserver":"10.1.11.11","server-pool":"10.1.11.111",
"service":"HTTP","https-service":"HTTPS","replacemsg":"Predefined","real-ip-addr":""}}
'''