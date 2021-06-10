# coding=utf-8
import urllib2
import cookielib


filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
# 利用HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 用handler来构建opener
opener = urllib2.build_opener(handler)
# 创建一个请求
request = opener.open("https://mail.wasu.com/")
# 保存cookie到文件
cookie.save(ignore_discard=True,ignore_expires=True)
