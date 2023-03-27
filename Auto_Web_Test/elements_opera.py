from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 主要获取属性的内容
wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.implicitly_wait(10)
wd.get('https://www.byhy.net/_files/stock1.html')

element = wd.find_element(By.ID,'suggestion')

test = element.get_attribute('placeholder')

print(test)


