# coding=utf-8
# selenium案例
import webbrowser

from selenium import webdriver

browser = webdriver.Chrome()
print browser
browser.get('http://www.baidu.com')



