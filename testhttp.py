import requests

ret = requests.get('https://github.com/timeline.json')

print ret.url
print ret.text