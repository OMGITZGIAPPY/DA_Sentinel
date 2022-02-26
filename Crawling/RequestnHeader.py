# Used of Request Library
import requests
# To have Agent Name as Mobile
headers = {'User-Agent' : 'Mobile'}

# Perform 'get' request & Display 'OK' return Status
url = "http://192.168.10.101/zipper/"
r = requests.get(url)
print(r.text)
print("Status code:")
if (r.status_code == 200):
    print("\t*","(" ,r.status_code,")", "OK")
# Display The Website Header
h = requests.head(url)
print("Header:")
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("******")

# To See User-Agent Display
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)