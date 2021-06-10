# coding=utf-8
import re

content = 'The 123456 is my on phone number The 123456 is my on phone number'
print (len(content))
result = re.findall(r'The\s(\d+)\sis', content)
print (result)
