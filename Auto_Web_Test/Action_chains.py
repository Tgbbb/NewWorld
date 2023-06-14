# 界面冻结调试代码：setTimeout(function(){debugger}, 5000)
# coding:utf-8
# 用Actionchains类里的方法去操作元素
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10) # 加这行就完事
wd.get('https://www.baidu.com/')

from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(wd).move_to_element(
    wd.find_element(By.CSS_SELECTOR,'[name=tj_settingicon]')
).perform()
# 前述语句只是描述这个操作，调用perform（）才会执行

input('xx')