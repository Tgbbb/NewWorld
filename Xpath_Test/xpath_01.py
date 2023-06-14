# xpath语法：
# 1、单斜杠/寻找直接子节点，

# 2、//双斜杠寻找相对子节点，包含在该节点下的内容

# 3、*通配符，寻找该节点下的所有子节点

# 4、根据属性来选择元素，示例：//*[@class = '123'],表示寻找所有节点下class属性 = 123的元素，*可以换成任意节点

# 5、因为xpath中属性默认是以完全匹配的方式寻找元素，所以要通过匹配部分来寻找元素需要使用语法//*[contains(@class,'123')],表示寻找所有节点下，class属性包含123的元素;

# //*[starts-with(@class,'123')]表示寻找所有节点下，class属性包含且以123开头的元素;同理//*[ends-with(@class,'123')],表示结尾且包含

# 6、根据排序寻找元素,示例 //div/p(2),表示寻找div节点下的第二个p属性元素，谨记不是div下第二个元素！倒序的方法类似//p(last()-1)

# 7、xpath的范围选择方法，position，可以用的时候去查看

# 8、通过webelement对象去做xpath语法寻找时，要在该对象里寻找就开头加个'.',示例.//p

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

elements = wd.find_elements(By.XPATH,'/html/body/div/span')

for data in elements:
    print(data.text)

