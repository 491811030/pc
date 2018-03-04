###Request对象传入urlopen，实现更复杂的请求

import urllib.request
request = urllib.request.Request('http://python.org')
response = urllib.request.urlopen(request)
#使用Request对象
#print(response.read().decode('utf-8'))

#完整Request

from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'Host':'httpbin.org'

}
#请求头User-Agent和Host
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req=request.Request(url = url,headers=headers,data=data)
#也可以使用req.add_header(''User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
#添加header
response = request.urlopen(req)
print(response.read().decode('utf-8'))