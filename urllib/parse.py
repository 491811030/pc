#分割,拆分url
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

#在url无协议类型时制定协议类型
from urllib.parse import urlparse
result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme = 'https')
print(type(result),result)
#制定了协议类型生效了
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme = 'https')
print(type(result),result)
#制定的协议类型未生效

from urllib.parse import  urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',allow_fragments = False)
#把fragments向前拼接
print(type(result),result)


from urllib.parse import  urlunparse
data = ['http','www.baidu.com','index.html','user','id=5','comment']
print(urlunparse(data))
#拼接url，urlparse的反函数


from urllib.parse import urljoin
#以后面的字段为基准，当某个字段在后面不存在时，从前面拿来补充
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','http://cuizhenyu.com/FAQ.html'))
print(urljoin('http://www.baidu.com','?category=2#comment'))



#urlencode可以把字典转换为一个请求参数
from urllib.parse import urlencode
params = {
    'name':'germey',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)

