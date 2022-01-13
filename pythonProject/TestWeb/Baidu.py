from selenium import webdriver


cdriver = webdriver.Chrome()

def run_baidu():

        cdriver.get('http://www.baidu.com')
        cdriver.find_element_by_id('kw').send_keys("重庆优路科技")
        cdriver.find_element_by_id('su').click()

run_baidu()
