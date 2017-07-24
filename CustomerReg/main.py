#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from CustomerReg.PO.base_page import BasePage
import  time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = '127。0.0.1:62001'
desired_caps['appPackage'] = 'com.quarkfinance.ufo'
desired_caps['appActivity'] = 'com.quarkfinance.ufo.ui.StartActivity'
desired_caps['app'] = "D:\Application\UFO_apk\ufo.apk"

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
Tpage=BasePage(driver)

# 向左滑动4个广告页面
for j in range(4):
    Tpage.swipeLeft(500)

#获取屏幕大小，通过相对位置点击‘立即体验’
time.sleep(3)
Page_Size=Tpage.getSize()
x=Page_Size[0]
y=Page_Size[1]
x_l = int((x, y)[0] * 0.5)
y_l = int((x, y)[1] * 0.893)
print x_l, y_l
TouchAction(driver).press(x=x_l, y=y_l).wait(200).release().perform()
#在首页点击 我的，进入登录页面，点击注册，进入注册页面
driver.find_element_by_id('profile_card').click()
driver.find_element_by_id('tv_register').click()

