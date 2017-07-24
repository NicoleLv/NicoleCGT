#coding=utf-8
from appium import  webdriver

class BasePage(object):

    def __init__(self,se_driver):
        self.driver=se_driver

    # 获取屏幕宽和高
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    # 向左滑动方法
    def swipeLeft(self,t):
        PaseSize=self.getSize()
        x1 = int(PaseSize[0] * 0.9)
        y1 = int(PaseSize[1] * 0.5)
        x2 = int(PaseSize[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, t)