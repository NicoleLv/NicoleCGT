#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from CustomerReg.PO.base_page import BasePage
import  time
import ConfigParser
import os


def Install_App(ConfigFile):

    #通过脚本当前路径拼接其他文件的路径函数
    PATH= lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


    #读取配置文件中app的信息，并赋值
    cf=ConfigParser.ConfigParser()
    cf.read(ConfigFile)
    desired_caps = {}
    desired_caps['platformName'] = cf.get('AppInf','platformName')
    desired_caps['platformVersion'] = cf.get('AppInf','platformVersion')
    desired_caps['deviceName'] = cf.get('AppInf','deviceName')
    desired_caps['appPackage'] = cf.get('AppInf','appPackage')
    desired_caps['appActivity'] = cf.get('AppInf','appActivity')
    desired_caps['app'] = PATH(cf.get('AppInf','app'))

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(3)
    Tpage=BasePage(driver)

    # 向左滑动4个广告页面
    for j in range(4):
        Tpage.swipeLeft(500)

    #获取屏幕大小，通过相对位置点击‘立即体验’进入首页
    time.sleep(3)
    Page_Size=Tpage.getSize()
    x=Page_Size[0]
    y=Page_Size[1]
    x_l = int((x, y)[0] * 0.5)
    y_l = int((x, y)[1] * 0.893)
    print x_l, y_l
    TouchAction(driver).press(x=x_l, y=y_l).wait(200).release().perform()
    return driver

if __name__=='__main__':
    Install_App()
