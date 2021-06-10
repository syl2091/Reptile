# coding=utf-8
# 模拟提交
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
print driver
print driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("syl")
elem.send_keys(Keys.RETURN)
print driver.page_source