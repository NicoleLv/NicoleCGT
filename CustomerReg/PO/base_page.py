#coding=utf-8
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import os,time


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

    #截图
    def screenshot(self,path):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        os.popen("adb wait-for-device")
        os.popen("adb shell screencap -p /data/local/tmp/tmp.png")
        if not os.path.isdir(path):
            os.makedirs(path)
        os.popen("adb pull /data/local/tmp/tmp.png " + (path + "/" + timestamp + ".png"))
        os.popen("adb shell rm /data/local/tmp/tmp.png")


    # 绘制手势密码
    def drawGestureCode(self):
        dic_size = self.driver.find_element_by_id("sudoku").size
        dic_loc = self.driver.find_element_by_id("sudoku").location
        step = dic_size['height'] / 4
        beginX = dic_loc['x'] + 2 * step
        beginY = dic_loc['y'] + 2 * step
        TouchAction(self.driver).press(x=beginX, y=beginY).wait(1000).move_to(x=step, y=0).wait(1000).move_to(x=0,
                                                                                                         y=step).wait(
            1000).move_to(x=-step, y=0).wait(1000).move_to(x=-step, y=0).wait(1000).release().perform()
