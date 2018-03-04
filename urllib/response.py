###response解析
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
#print(type(response))
#输出response的类型

import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
#status和getheaders是请求成功的标志，getheaders返回一个元组对的列表，
#可以通过gethead函数来查询值
print(response.getheader('Server'))