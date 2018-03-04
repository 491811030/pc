
###urllib.request.urlopen的前三个参数
import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
#print(response.read().decode('utf-8'))
#respondse.read()返回的byte类型的响应体，需要decode到特定编码。



##以post形式传入数据
import urllib.parse
import urllib.request
data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
#post数据要预先加工，从utf-8到parse.urlencode到bytes
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#带data参数就post
#这是一个做http测试网址
#print(response.read().decode('utf-8'))
import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get',timeout = 1)
print(response.read())


import socket
import urllib.requet
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    #timeout的错误类型属于urllib.error.URLError
    #原因是socket.timeout
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')