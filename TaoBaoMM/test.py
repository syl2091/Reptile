import urllib
import urllib2
import re
import tool
import os


try:
    url = 'https://v.taobao.com/v/content/live?catetype=704&from=taonvlang&page=4'
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    request = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(request)
    print response.read()
except Exception as e:
    if hasattr(e,'reason'):
        print e.reason