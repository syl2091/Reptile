# coding=utf-8
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie 之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
data = urllib.urlencode({
    'uid':'shenyongl@wasu.com',
    'pwd':'syl2091...',
    'lang':'SIMPLIFIED_CHINESE',
    'style':'enterprise2'
})
# 登录url
loginUrl = 'https://mail.wasu.com/'
# 模拟登录
result = opener.open(loginUrl , data)
# 保存cookie到cookie.txt 中
cookie.save(ignore_discard=True,ignore_expires=True)
# 利用cookie去访问另外网址
mailUrl = 'https://mail.wasu.com/tmw/37/next/loading.jsp?sessionid=347801cH3f2_0'
result = opener.open(mailUrl)
print result.read()