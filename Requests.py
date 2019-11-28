#-*- coding: utf-8 -*- 

import requests
import json

r = requests.get('https://api.github.com/user', auth=('qixqi', '******'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
print('\n'*3)


r = requests.get('https://qixqi.club')
print(r.text)
print(r.encoding)
print(r.url)
print(r.status_code)
print('\n'*3)


# GET 参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
r.encoding = 'UTF-8'        # 编码
results = json.loads(r.text)
print(results['args'])
print('\n'*3)


# POST 参数
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
results = json.loads(r.text)
print(results['args'])
print('\n'*3)