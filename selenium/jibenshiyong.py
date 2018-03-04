##基本使用
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
browser = webdriver.PhantomJS()#声明浏览器对象
try:
    browser.get('http://www.baidu.com')#传入网址
    input= browser.find_element_by_id('kw')#查找
    input.send_keys('Python')#像元素里发送键
    input.send_keys(Keys.ENTER)#再发送回车
    wait = WebDriverWait(browser,10)#浏览器等待
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    #等待直到By。ID是content_left加载出来
    print(browser.current_url)#打印出当前url
    print(browser.page_source)#打印出当前源代码
    print(browser.get_cookies())#打印出当前cookie
finally:
    browser.close()