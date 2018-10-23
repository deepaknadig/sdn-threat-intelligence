import http.client
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

conn = http.client.HTTPSConnection("localhost")

payload = ""

headers = {
    'authorization': "",
    'accept': "application/json",
    'content-type': "application/json"
    }

conn.request("GET", "/attributes/bro/download/ip", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
