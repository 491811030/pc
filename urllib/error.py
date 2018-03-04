
# from urllib import request,error
# try:
#     response = request.urlopen('http://cuizheyu.com')
# except error.URLError as e:
#     #URLError是父类异常,只有一个reason属性
#     print(e.reason)

from urllib import error,request
try:
    request.urlopen('http://cuizhenyu.com')
except error.HTTPError as r:
    print(r.reason,'+',r.code,'+',r.headers,sep='\n')
    #有三个属性
except error.URLError as e:
    print(e.reason)

#判断异常原因
import socket
import urllib.error
import urllib.request
try:
    response = request.urlopen('http://www.baidu.com',timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')