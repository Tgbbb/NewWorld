# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#练习1
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "JJLZ9H9HJBBMGMKF"
caps["platformVersion"] ="12"
caps["appPackage"] = "com.youloft.calendar"
caps["appActivity"] = "com.youloft.LauncherActivity"
caps["automationName"] = "uiautomator2"
caps["newCommandTimeout"] = "60"
caps["noReset"] = "true"
#caps["ensureWebviewsHavePages"] = True
#默认同意弹窗
caps["autoAcceptAlerts"] = True

#发送指令到appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#强制等待20s
time.sleep(10)
#日历切换，点击万年历tab
Calendar = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("万年历")')
Calendar.click()
time.sleep(3)
#选择传统万年历
Calendar1 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("星座日历")')
Calendar1.click()
time.sleep(3)
#点击天气
weather = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("天气")')
weather.click()
#点击+
weather1 = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.youloft.calendar:id/city_check"]/android.widget.ImageView[1]')
weather1.click()
time.sleep(3)
#点击添加城市
weather2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("添加城市")')
weather2.click()
time.sleep(3)
#选择沈阳
weather3 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("沈阳")')
weather3.click()
time.sleep(3)
#点击编辑
weather4 = driver.find_element(AppiumBy.ID,"com.youloft.calendar:id/actionbar_button")
weather4.click()
time.sleep(2)
#勾选沈阳
weather5 = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.youloft.calendar:id/list_view"]/android.view.ViewGroup[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
weather5.click()
time.sleep(1)
#点击完成
weather6 = driver.find_element(AppiumBy.ID,"com.youloft.calendar:id/actionbar_button")
weather6.click()
time.sleep(3)
#点击返回
weather7 = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.youloft.calendar:id/actionbar_back"]')
weather7.click()

#rili= driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("万年历")')
#rili.click()
#od= driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("每日一言")')
#driver.find_elements()
