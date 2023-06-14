from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = wd.find_element(By.CSS_SELECTOR,
                          '.plant')
# 1、#id值 用来标记属性id的元素
# 2、.class值 用来标记属性class的元素
# 3、选择tag名，直接就”tag名“就行
# 4、通过属性值寻找元素 '[href=xxxx]',href为属性名
# 层级问题，用 > 连接，只能连接父级和直接子元素，当父元素连接后代元素时会无法找到；用 空格 连接可以连接子元素和后代元素
# 表达式之间可以组合使用，只要层级关系正确
# 用逗号，表示表达式的或关系；逗号的每一层都是单独的
# ！重*要！按次序选择子节点，nth—child，限定条件的第几个元素，例如 span:nth-child(2),意思是包含span的父元素下的第二个节点，且只有这个节点是span的时候才能正确找到。  :nth-child(2)冒号前没有限定时，代表所有父节点下第二个元素..注意：当标记的位置不是限定元素时，无法找到
# 指定第几个某类型的子节点，比如 span:nth-of-type选择的是第一个span类型的子元素，与nth-child有本质区别，nth-last-of-type倒数.
# nth-child(even) even选择偶数节点，odd选择奇数节点，前面也可以限定元素类型 p:nth-child(even)  选择所有节点中的偶数并且是p类型， p:nth-of-type(even)  选择p类型节点中的偶数节点
# 用+号连接，选择该子节点，用~号连接，选择该属性下所有子节点

print(element.text)
