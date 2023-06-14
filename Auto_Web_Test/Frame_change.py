# 改节介绍Frame切换的方法
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
wd.implicitly_wait(10)

# 有元素在Frame属性中时，Frame：html中嵌套的另外一个html，需要切换到对应的Frame才能获取到其中的元素

wd.switch_to.frame('frame1')
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')

for i in elements:
    print('------------------')
    print(i.get_attribute('innerHTML'))
# 切换到内层后，就只会在这一层捕捉操作元素，其它层的需要切换回去，如下代码:
wd.switch_to.default_content()
element = wd.find_element(By.ID, 'outerbutton')
element.click()

input('输入任意字符结束:')
