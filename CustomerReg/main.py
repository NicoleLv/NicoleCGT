#coding=utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from CustomerReg.PO.base_page import BasePage
import  time
import ConfigParser
import os
from Basic_oper.Excel_oper import Excel_file


#通过脚本当前路径拼接其他文件的路径函数
PATH= lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#读取配置文件中app的信息，并赋值
cf=ConfigParser.ConfigParser()
cf.read('Reg_Config')
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

#从外部excel文档读取待注册数据
RegFile=cf.get('TestData','DataFile_Path')
RegSheetName=cf.get('TestData','SheetName')
AccountToReg=Excel_file()
rows=(AccountToReg.Get_FileInf(RegFile,RegSheetName))[0]
cols=(AccountToReg.Get_FileInf(RegFile,RegSheetName))[1]

#获取客户类型，调用不同的方法注册
for i in range(rows-1):


