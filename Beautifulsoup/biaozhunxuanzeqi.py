####标准选择器

##find_all(name,attrs,recursive,text,**kwargs)
# 可根据标签名、属性、内容查找
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from  bs4 import  BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all('ul'))
#find_all返回一个列表
for ur in soup.find_all('ul'):
    print(ur)
print(type(soup.find_all('ul')[0]))


##find_all的attrs参数指定某些属性查找
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={'id':'list-1'}))
#传入字典形式的值
print(soup.find_all(attrs={'name':'elements'}))


###直接查找一个属性
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(id='list-1'))
print(soup.find_all(class_= 'element'))
#注意这里的class后面带一个下划线，为了和类区分

##text
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(text='Foo'))
#text返回的是内容
##find函数返回单个元素，find_all返回所有元素，
##find_parents()返回所有祖先节点，find_parent()返回父节点
##find_next_siblings() find_next_sibling()find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
##find_previous_siblings() find_previous_sibling()find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点
##find_all_next() find_next()find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
##find_all_previous() 和 find_previous()find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点


####CSS选择器
##通过select（）直接传入CSS选择器即可完成选择
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))
#注意css格式的class参数前面有个点，点之间有空格
print(soup.select('div ul'))
#css格式各个标签之间有空格,空格前面都是上一级别
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))


###获取属性
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import  BeautifulSoup
soup = BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    #直接用中括号获取属性
    print(ul.attrs['id'])
    #用attrs获取属性



###get_text()获取内容
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from  bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
for li in soup.select('li'):
    print(li.get_text())