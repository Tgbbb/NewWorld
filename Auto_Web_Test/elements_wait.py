# web自动化中时间等待的方法
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10) # 加这行就完事
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID, 'kw')  # element对象，生成一个捕捉到的元素的对象
element.send_keys('通讯\n')
element = wd.find_element(By.ID, 'go')
element.click()
element = wd.find_element(By.ID, '1')
print(element.text)
# 复杂操作，自己写的.自带的等待元素的方法，在顶部加一行implicitly,隐
# while True:
#     try:
#         element = wd.find_element(By.ID, '1')
#         print(element.text)
#         break
#     except:
#         time.sleep(1)

