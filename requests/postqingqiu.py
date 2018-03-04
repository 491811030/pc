###基本post请求

import requests
data = {'name':'germey','age':'22'}
response = requests.post('http://httpbin.org/post',data = data)
print(response.text)
##加上headers
data = {'name':'germey','age':'22'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
response = requests.post('http://httpbin.org/post',data = data,headers=headers)
print(response.json())