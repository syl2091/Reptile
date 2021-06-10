import requests

url = 'http://example.com'
r = requests.get(url)
print r.cookies



url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text


r = requests.get('https://github.com', timeout=0.001)

print r.text