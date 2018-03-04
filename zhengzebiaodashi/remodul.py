####re模块实例

###re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match（）就返回none
#re.match(pattern,string,flags=0)
import re
content  = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
#\s匹配一个不可见字符，\d匹配一个数字字符，后面加个大括号表示匹配几次
#.匹配\r\n之外的任意字符，*表示匹配前面子表达式任意次，$确定结尾的字符
print(result.group())
#返回匹配结果字符
print(result.span())
#返回匹配结果范围

##泛匹配
import  re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('Hello.*Demo$',content)
print(result.group())
print(result.span())

##匹配目标
import re
content =  'Hello 1234567 World_This is a Regex Demo'
result = re.match('Hello\s(\d+)\sWorld.*Demo$',content)
print(result)
print(result.group(1))
#group（1）返回第一个小括号的匹配出的内容
print(result.span())

##贪婪匹配
import re
content =  'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
#.*会尽可能的匹配多，只留给\d+一个7

##非贪婪匹配
import re
content =  'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))
#.*后面加个问号会匹配尽可能的少的字符，所以\d+返回1234567


##匹配模式
import re
content =  '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*Demo$',content,re.S)
#.*无法匹配换行，必须加上re.S
print(result.group(1))

##转义
import re
content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
#在字符串中要匹配特殊字符
print(result)

###re.sreach 扫描整个字符串并返回第一个成功的匹配
import re
content =  'Extra stings Hello 1234567 World_This is a Regex Demo'
result = re.match('Hello.*?(\d+).*Demo$',content)
print(result)
#match匹配失败
result = re.search('Hello.*?(\d+).*Demo$',content)
#search匹配成功
