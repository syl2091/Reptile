# coding=utf-8
# bs4案例
from bs4 import BeautifulSoup
import requests

html = requests.get("http://www.baidu.com").text
print html
soup = BeautifulSoup(html)
print soup.prettify()
print soup.head
print soup.div
print soup.div.get('id')
print soup.title.string