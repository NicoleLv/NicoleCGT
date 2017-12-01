#coding=utf-8
import requests
import time
from CustomerReg.PO.GetVerifyCode import Get_VerifyCode
from CustomerReg.Open_App import Install_App

class Cus_HFKH(object):

    def __init__(self,driver):
        self.driver=driver

     #恒丰委托开户页面获取验证码，点击提交，做恒丰开户
    def Cus_HFKH(self,PhoneNum):
        self.driver.find_element_by_id('tv_getverify').click()
        VerifyCode=Get_VerifyCode(PhoneNum) #到短信平台获取验证码
        self.driver.find_element_by_id('edit_code').send_keys(VerifyCode)
        self.driver.find_element_by_id('tv_commit').click()
        # self.driver.implicitly_wait(20)



    #设置交易密码
    def Set_TransPassword(self,TransactionPassword):
        #APP中嵌入html5可以用下面的方法转换，在chrome浏览器打开获取元素属性
        # chrome://inspect/#devices  谷歌浏览器打开
        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)

        time.sleep(1)
        self.driver.find_element_by_id('pwd').send_keys(TransactionPassword)
        self.driver.find_element_by_id('pwdC').send_keys(TransactionPassword)
        self.driver.find_element_by_id('verify_info').send_keys('jhg')
        self.driver.find_element_by_class_name('save_btn').click()


if __name__=='__main__':
    driver=Install_App('..\Reg_Config')
    #登录需要开户的账号
    driver.implicitly_wait(120)
    driver.find_element_by_id('profile_card').click()
    driver.find_element_by_id('edit_name').send_keys('14477880030')
    driver.find_element_by_id('edit_password').send_keys('qwe123')
    driver.find_element_by_id('tv_login').click()
    time.sleep(1)
    driver.find_element_by_id('btn_right').click()

    KH=Cus_HFKH(driver)
    KH.Cus_HFKH('14477880030')
    KH.Set_TransPassword('qwe123')







