###基本交互操作
##查找元素
#单个元素
# from selenium import webdriver
# browser = webdriver.PhantomJS()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')#？
# input_third = browser.find_element_by_xpath('//*[@id="q"]')#?
# #这三个找到的是等价的
# print(input_first,input_second,input_third)
# browser.close()


###通用的查找方式
# from selenium import webdriver
# from  selenium.webdriver.common.by import By
# browser = webdriver.PhantomJS()
# browser.get('http://www.taobao.com')
# input_first = browser.find_element(By.ID,'q')#通用的查找方式，用By取代
# print(input_first)
# browser.close()
#
# ##查找多个元素
# from selenium import  webdriver
# from  selenium.webdriver.common.by import By
# browser = webdriver.PhantomJS()
# browser.get('http://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li')
# lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')#以列表形式返回
# print(lis)
# browser.close()

####元素交互操作
# from selenium import  webdriver
# import  time
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# #Pantom存在无法点击问题，用Chrome就可以点击。chrome里面ctrl+f去找标签。
# browser.get('http://www.taobao.com')
# input = browser.find_element_by_id('q')#取得输入框
# input.send_keys('iPhone')#对输入框输入
# time.sleep(1)
# input.clear()#清空输入框
# input.send_keys('iPad')#对输入框输入
# button = browser.find_element_by_class_name('btn-search')#取得按钮 ,标签中class中空格表示且的关系
# button.click()#在css样式的class中.a .b表示层次关系。
# #还有更多操作在文档中。


###交互动作，将动作附加到动作链中
###CSS选择中#是ID选择器 .是class选择器 *是通配符号
# from  selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')##CSS选择中井号表示对id的选择，点表示对class的选择。
# target = browser.find_element_by_css_selector('#droppable')##一个标签的样式用css确定，可以是id，也可以是class
# actions = ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()
# 更多操作在网站中
#
# ##执行JavaScript,直接利用接口执行JavaScript语句
# from selenium import webdriver
#
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.get('http://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


###获取元素信息

###获取属性
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# url = 'http://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))


###获取文本值
# from selenium import webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

###ID,位置，标签名，大小
# from selenium import  webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# url = "http://www.zhihu.com/explore"
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

###frame,有一些元素在子frame中，不能直接由网页得到
# import  time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')##转入子frame
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No Logo')
# browser.switch_to.parent_frame()##返回父frame
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

###等待,有一些AJax操作，元素需要时间才能加载出来
##Ajax是异步刷新，不用重新加载全部页面，只加载部分页面，可以用javascript写
##隐式等待,如果WebDriver没有在DOM中找到元素，将继续等待，如果超出了设定时间，则返回异常。
# from selenium import webdriver
# browser =webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)

###显示等待,指定一个等待条件和最长等待时间
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import  expected_conditions as EC
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser,10)
# input= wait.until(EC.presence_of_element_located((By.ID,'q')))##指定元组元素加载出
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))##元素可点击
# print(input,button)
#
# ##更多在网站中。

###前进后退
# import time
# from selenium import  webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.get('https://www.baidu.com')
# browser.get('http://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

###cookies
# from selenium import webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

###选项卡管理
# import time
# from selenium import webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.get('http://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('http://python.org')

###异常处理
# from selenium import  webdriver
# browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
# browser.find_element_by_id('hello')

from selenium import  webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

##具体详细异常在网页中可查