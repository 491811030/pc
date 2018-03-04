##Ajax技术加载部分网页，下拉不断增加就增加页面就是Ajax技术
##网络库requests,解析库Beautiful Soup，正则表达式，存储数据库MONGDB
import re
import requests
import json

from bs4 import BeautifulSoup

from urllib.parse import urlencode
from requests.exceptions import RequestException

def get_page_index(offset,keyword):##成功调用了一个Ajax请求，类似于一个小规模的url请求
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,


    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    ##urlencode可以把字典对象转化为url的请求参数
    try:
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data'in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        print(url)
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('出错')
        return None

def parse_page_detail(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('var gallery = (.*?);',re.S)
    result = re.search(images_pattern,html)
    if result:
        print(result.group(1))
def main():
    html = get_page_index(0,'街拍')

    for url in parse_page_index(html):
        html = get_page_detail(url)



if __name__ == '__main__':
    main()
