import requests
##通过查询文档得知最大的异常是RequestException，所以可以直接写一个
# RequestException就行了
from requests.exceptions import RequestException
from  multiprocessing import  Pool##利用多进程是先秒抓
import re
import json
def get_one_page(url):
    try:
        response = requests.get(url)
        print(response.text)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)#re.S使点可以匹配换行符
    items = re.findall(pattern,html)
    for item in items:##使函数变成一个生成器
        yield{
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],#strip函数去除空白符
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]

        }
##写入文件
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        ##encoding文件编码和解码的编码方式
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        ##ensure——ascii为了输出中文
        f.close()
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        #write_to_file(item)

if __name__ =='__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    ##此函数将后面列表中的每一个元素当作前面函数的参数
    ##多进程乱码问题