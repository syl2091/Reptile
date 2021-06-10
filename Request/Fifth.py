# coding=utf-8
# 使用cookie模拟会话

import requests

s = requests.session()
s.headers.update({'x-text':'true'})
r = s.get('http://httpbin.org/headers',headers={'x-test2': 'true'})
print r.text