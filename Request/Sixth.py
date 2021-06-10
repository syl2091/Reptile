# coding=utf-8
# SSL证书验证


import requests


# r = requests.get('https://github.com',verify=False)
# print r.text

# 代理
proxies = {
    "https":"http://41.118.132.69:4433"
}
r = requests.get('http://httpbin.org/post',proxies=proxies)
print r.text