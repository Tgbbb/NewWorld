# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
# wd = webdriver.Chrome(service=Service('../chromedriver.exe'))

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')  # webdriver的get方法获取你要的网站 ,股票示例页面：https://www.byhy.net/_files/stock1.html
# 通过类型名class去定位元素
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# element = wd.find_element(By.CLASS_NAME, 'animal')  # find_element和find_elements的区别，一个返回一个元素对象，一个返回的是列表的对象
# elements本身调用find_elements返回的是一个列表对象，所以也可以调用webelement的所有方法，缩小范围进行第二层的元素定位
# 如下：test = elements.find_elements(By.TAG_NAME, 'span')

for element in elements:
    print(element.text)
# 通过标签名tag去定位元素
elements = wd.find_elements(By.TAG_NAME, 'span')
for element in elements:
    print(element.text)


# element = wd.find_element(By.ID, 'kw1')  # element对象，生成一个捕捉到的元素的对象
# element.send_keys('通讯\n')
# try:
#     element = wd.find_element(By.ID, 'kw') # element对象，生成一个捕捉到的元素的对象
# except NoSuchElementException:
#     print('找不到该字符')
# element.send_keys('通讯')
# element = wd.find_element(By.ID, 'go')
# element.click()
#
# input('输入任意字符结束程序:')

# 等待网页响应的方法

