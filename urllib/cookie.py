import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
#创建一个收集cookie的对象
handler = urllib.request.HTTPCookieProcessor(cookie)
#创建一个收集cookie的handler
opener = urllib.request.build_opener(handler)
#用带作用的handler创建一个打开器
response = opener.open('http://www.baidu.com')
#打开网站的同时也自动获取到了cookie
for item in cookie:
    print(item.name+'='+item.value)


#把cookie保存为文本文件保持登陆状态
import http.cookiejar,urllib.request
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
#MozillaCookieJar是CookieJar的子类，用save方法把cookie保存为文本文档
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)


#另一种cookie保存格式
import http.cookiejar,urllib.request
filename = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

#读取cookie，读取和存储格式要一致
import http.cookiejar,urllib.request
cookie = http.cookiejar.MozillaCookieJar()
#cookie对象有一个load功能载入已经存储的cookie

cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler =urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))