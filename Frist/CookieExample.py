# coding=utf-8
import urllib2
import cookielib

# 声明一个cookiejar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for ietm in cookie:
    print 'Name = ', ietm.name
    print 'Value = ',  ietm.value
