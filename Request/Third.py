import requests

url = 'http://httpbin.org/post'
files = {'file': open('D:\\pcopt\\Reptile\Request\\test.text', 'r')}
r = requests.post(url, files=files)
print r.text