import json

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=json.dumps(payload))
print r.text