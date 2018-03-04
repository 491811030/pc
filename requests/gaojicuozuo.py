###request高级操作


##文件上传
# import requests
# files = {'file':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)

##获取cookie
import  requests
response = requests.get('http://www.baidu.com')
print(response.cookies)
#cookie是一个列表的形式
for key,value in response.cookies.items():
    print(key+'='+value)

##会话维持，模拟登陆
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
#此处为设置cookie
response = requests.get('http://httpbin.org/cookies')
#此处返回的cookie为空，因为前面设置cookie与此处的相当于两个不同的浏览器
#如果想要同一，就要用下面Session对象
print(response.text)

#利用Session统一浏览器,主要用于登陆后的信息获取
import requests
s=requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

##证书验证，https会是不安全，返回SSL认证错误
import requests
response = requests.get('http://www.12306.cn')
print(response.text)

#利用参数verify可以避免这个问题
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
#如果没有此句系统会弹出警告，希望你验证网站
response = requests.get('https://www.12306.cn',verify=False)
print(response.text)

#手动设置证书,需要本地的一个证书
# import  requests
# response = requests.get('http://www.12306.cn',cert=('/path/server.crt','/path/key'))
# print(response.status_code)


##代理设置
import requests
proxies = {
    'http':'http://122.114.31.177:808'
}

response = requests.get('https://www.taobao.com',proxies=proxies)
print(response.status_code)

#需要用户名和密码的代理
# import requests
# proxies = {
#     'http':'http://user:password@122.114.31.177:808'
# }
# response=requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)

#如果代理是sock类型的,先pip install 'request{socks}'
# import requests
# proxies = {
#     'http':'socks5://127.0.0.1:9742',
#     'https':'sock5://127.0.0.1:9472'
# }
# response =requests.get('http://taobao.com',proxies=proxies)

##超时设置
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get('https://www.taobao.com',timeout=1)
    #规定时间内服务器没应答就抛出ReadTimeout异常
    print(response.status_code)
except ReadTimeout:
    print('TIMeout')

##认证设置,进入网站时就要输入用户名，密码
import requests
from  requests.auth import HTTPBasicAuth
#此模块用于传入用户名和密码
r =requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
#auth参数一个有用户名和密码的basicauth对象
print(r.status_code)

#借用字典传入auth
import requests
r=requests.get('http://120.27.34.24:9001',auth={'user':'123'})
print(r.status_code)


##异常处理
import requests
from requests import ReadTimeout,HTTPError,RequestException
#requestexception是父类
try:
    response = requests.get('http:httpbin.org/get',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('TIme out')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')