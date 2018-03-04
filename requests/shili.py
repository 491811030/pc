###实例
import  requests
response = requests.get('http://www.baidu.com')
print(type(response))
#对象类型
print(response.status_code)
#状态码
print(type(response.text))
#返回字符串类型
print(response.text)
print(response.cookies)


