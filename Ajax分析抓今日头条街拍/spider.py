##Ajax技术加载部分网页，下拉不断增加就增加页面就是Ajax技术
##网络库requests,解析库Beautiful Soup，正则表达式，存储数据库MONGDB
import re
import requests
import json
import pymongo
from config import *
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError
import os
from hashlib import md5
from multiprocessing import Pool
from urllib.parse import urlencode
from requests.exceptions import RequestException

client = pymongo.MongoClient(MONGO_URL,connect=False)
#多进程下可能重复链接MONGODB报错，用connnect=False解决
db = client[MONGO_DB]
def save_to_mongo(result):
    #存储到MONGODB
    if db[MONGO_TABLE].insert(result):
        print('存储成功')
        return True
    return False

def get_page_index(offset,keyword):##成功调用了一个Ajax请求，类似于一个小规模的url请求
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'from':'gallery'


    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    ##urlencode可以把字典对象转化为url的请求参数,执行Ajax返回的response是Ajax的response
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('出错')
        return None

def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data'in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass

def get_page_detail(url):
    try:

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}

        response = requests.get(url,headers = headers)

        if response.status_code == 200:
            return response.text

    except RequestException:
        print('出错')
        return None

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    #select选择所有title标签返回列表。
    print(title)
    images_pattern = re.compile('gallery: JSON\.parse\("(.*?)"\),',re.S)
    result = re.search(images_pattern,html)
    #re.search()函数将对整个字符串进行搜索，并返回第一个匹配的字符串的match对象，对象的group（n），是第n个要得到的字符串。
    #re.findall()函数将返回一个所有匹配的字符串的字符串列表。

    result=result.group(1).replace('\\','')
    if result:
        data = json.loads(result)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            return{
                'title':title,
                'url':url,
                'images':images
            }


def download_image(url):
    print('下载',url)
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}
        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            save_image(response.content)
            #contene返回二进制，text返回文本
    except RequestException:
        print('tupian出错')
        return None


def save_image(content):
    file_path = '{0}/{1}/{2}.{3}'.format(os.getcwd(),'picture',md5(content).hexdigest(),'jpg')
    # md5防止重复下载，在程序出错等情况下
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            #存储文件以二进制方式
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset,KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result= parse_page_detail(html,url)
            save_to_mongo(result)



if __name__ == '__main__':

    groups = [x*20 for x in range(GROUP_START,GROUP_END * 1)]
    pool = Pool()
    pool.map(main,groups)
