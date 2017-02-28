import requests
import json

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

ret = requests.post(url, data=json.dumps(payload), headers=headers)

print ret.text
print ret.cookies