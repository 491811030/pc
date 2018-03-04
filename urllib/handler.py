#handler是各种辅助函数

#代理，伪装自己的ip地址，以免被服务器封锁
import urllib.request
proxy_headler = urllib.request.ProxyHandler({
    'http':'http://113.207.44.70:3128',
    'https':'https://123.125.159.122:80'

})
#输入代理ip和端口
opener = urllib.request.build_opener(proxy_headler)
#urllib.request.open的参数进行设置
response = opener.open('http://httpbin.org/get')
#opener.open也可以传入Request对象
print(response.read().decode('utf-8'))


#cookie是存储在客户端的一个记录用户身份的一个文本文件（主要是维持登陆状态）
