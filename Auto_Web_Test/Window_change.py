# 改节介绍窗口之间切换的方法
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

element = wd.find_element(By.CSS_SELECTOR, '[href = "http://www.bing.com"]')
element.click()
# 通过窗口标签页的句柄去跳转到对应窗口
for handle in wd.window_handles:  # window.handles为web driver的一个方法，可以获得当前浏览器中所有的标签页，循环当前浏览器中所有的标签页，再去判断每个标签页的标题中是否有想要的，就可以跳转对应标签了
    wd.switch_to.window(handle)  # switch_to.window为跳转窗口的方法
    if 'Bing' in wd.title:
        break
element = wd.find_element(By.ID, 'sb_form_q')
element.send_keys('The Legend of Zelda')
element = wd.find_element(By.CSS_SELECTOR, '[viewBox="0 0 25 25"]')
element.click()

input('输入任意字符结束:')
