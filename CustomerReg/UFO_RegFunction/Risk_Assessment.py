#coding=utf-8
import  time
import random

class Risk_Assessment():

    def __init__(self,driver):
        self.driver=driver

    def Risk_Assessment(self):
        time.sleep(2)
        webview_RA=self.driver.contexts[-1]
        self.driver.switch_to.context(webview_RA)
        #chrome://inspect/#devices  谷歌浏览器打开获取页面元素属性
        # 风险评估前9个页面
        for i in range(9):
            j = random.randint(0, 3)
            time.sleep(1)
            self.driver.find_elements_by_name("SubjectItem")[j].click()
            time.sleep(1)
            self.driver.find_element_by_id('aNextSubject').click()
        # 风险评估最后一个页面，结束后点击完成
        j = random.randint(0, 3)
        time.sleep(1)
        self.driver.find_elements_by_name("SubjectItem")[j].click()
        time.sleep(1)
        self.driver.find_element_by_id('aComplete').click()
        driver.find_element_by_id('tb_goBack').click() #点击返回，评估结束

if

