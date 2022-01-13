from selenium import webdriver


class run_case(object):
    def __init__(self):
        self.C_driver = webdriver.Chrome()

    def run_baidu(self):
        self.C_driver.get("http://www.baidu.com")

        self.C_driver.find_element_by_xpath('//*[@id="kw"]').send_keys("Cypress端到端")
        self.C_driver.find_element_by_id('su').click()
        val_text = self.C_driver.find_element_by_xpath('//*[@id="su"]').text
        print(val_text)
        val_size = self.C_driver.find_element_by_xpath('//*[@id="su"]').size
        print(val_size)
        val_get_attribute = self.C_driver.find_element_by_xpath('//*[@id="su"]').get_attribute
        print(val_get_attribute)
        self.C_driver.back()
        self.C_driver.refresh()
        self.C_driver.forward()
        self.C_driver.quit()


if __name__ == '__main__':
    run_case().run_baidu()