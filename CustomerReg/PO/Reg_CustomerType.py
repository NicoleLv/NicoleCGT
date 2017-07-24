#coding=utf-8
from appium import  webdriver

class Select_CusType  (object):


    def __init__(self,se_driver):
        self.driver=se_driver

    def CusType_selected(self,CusType):
        self.driver.find_element_by_name(CusType).click()

