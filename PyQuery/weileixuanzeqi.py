###伪类选择器

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import  PyQuery as pq
doc = pq(html)
li  = doc('li:first-child')
print(li)
#获取标签下第一个孩子
li = doc('li:last-child')
#获取最后一个孩子
print(li)
li= doc('li:nth-child(2)')
#获取第2个孩子
print(li)
li = doc('li:gt(2)')
#获取比2大的
print(li)
li = doc('li:nth-child(2n)')
#获取2的倍数
print(li)
li = doc('li:contains(second)')
#包含second文本的li标签
print(li)