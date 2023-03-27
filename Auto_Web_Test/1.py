# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
# wd = webdriver.Chrome(service=Service('../chromedriver.exe'))

wd.get('https://www.byhy.net/_files/stock1.html')  # webdriver的get方法获取你要的网站

# element = wd.find_element(By.ID, 'kw1')  # element对象，生成一个捕捉到的元素的对象
# element.send_keys('通讯\n')
try:
    element = wd.find_element(By.ID, 'kw') # element对象，生成一个捕捉到的元素的对象
except NoSuchElementException:
    print('找不到该字符')
element.send_keys('通讯')
element = wd.find_element(By.ID, 'go')
element.click()

input('输入任意字符结束程序:')
