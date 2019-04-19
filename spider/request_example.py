#!/usr/bin/python
# coding: utf-8

import requests

r = requests.get('http://www.santostang.com/')

print(r.encoding)
print(r.status_code)
# print(r.text)

# requests get -> params={dict}
# requests post -> data={dict}
# headers={dict}
# timeout={second}

# get request
key_dict = {'key1': 'key1', 'key2': 'key2'}
r = requests.get('https://httpbin.org/get', params=key_dict)
print(r.url)
# print(r.text)

# post request
key_dict = {'key3': 'key3', 'key4': 'key4'}
r = requests.post('https://httpbin.org/post', data=key_dict, timeout=1)
print(r.status_code)
print(r.text)
