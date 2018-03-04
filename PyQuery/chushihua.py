####初始化


###字符串初始化
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from  pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))
#返回的是对象

doc = pq(url='http://www.baidu.com')
print(doc('head'))


###url初始化
from pyquery import  PyQuery as pq
doc = pq(url = 'http://www.baidu.com')
print(doc('head'))

#
# ###文件初始化
# from pyquery import PyQuery as  pq
# doc = pq(filename='demo.html')#filename参数得到的是文件路径
# print((doc('li')))