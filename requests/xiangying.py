###响应

##response的属性
import requests
response = requests.get('http://www.jainshu.com')
print(type(response.status_code),response.status_code)
print(type(response.headers),response.headers)
print(type(response.cookies),response.cookies)
print(type(response.url),response.url)
print(type(response.history),response.history)

##状态码判断
import requests
response = requests.get('http://www.jianshu.com')
#exit() if not response.status_code == requests.codes.ok else print('Request Successfully')
#状态字符ok可以直接与返回的状态码比较
exit() if not response.status_code == 404 else print('404')