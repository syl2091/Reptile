# coding=utf-8
import cookielib
import urllib2


# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# 创建请求
request = urllib2.Request("http://www.baidu.com")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()