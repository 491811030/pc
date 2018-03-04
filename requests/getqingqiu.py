##基本get请求
import requests
response = requests.get('http://httpbin.org/get')
print(response.text)

##带参数get请求
import requests
response = requests.get('http://httpbin.org/get?name=gemey&age=22')
#get参数在末尾问号后面拼接，用&分隔
print(response.text)

##params传参数方法
import requests
data = {
    'name':'germey',
    'age': 22
}
#以字典的方式传送参数
response = requests.get('http://httpbin.org/get',params = data)
print(response.text)

##解析json，json是把数据和字符串进行转换，然后就可以进行传递。
##json.dumps : dict转成str，
## 后两个是带文件参数的，作用存在文件上 json.dump是将python数据保存成json存入文件，json.loads:str转成dict          json.load是读取json数据
import requests
import json
response = requests.get('http://httpbin.org/get')
#返回结果是json
print(type(response))
print(response.json())
#实际上就是执行了json.loads方法
print(json.loads(response.text))
print(type(response.json()))

##获取二进制数据
import requests
response=requests.get('http://github.com/favicon.ico')
print(type(response.text),type(response.content))
#respponse.content就是二进制内容
print(response.text)
print(response.content)
#保存二进制
# import requests
# response = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()


##添加headers,避免被拒绝
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}
response = requests.get('http://zhihu.com/explore',headers=headers)
print(response.text)