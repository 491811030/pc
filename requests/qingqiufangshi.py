###请求方式
import requests
print(requests.post('http://httpbin.org/post').text)
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')