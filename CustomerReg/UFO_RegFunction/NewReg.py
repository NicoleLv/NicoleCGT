#coding=utf-8
from appium import webdriver
from CustomerReg.Open_App import Install_App
import time,os
from CustomerReg.Basic_oper.RandomData_Gern import Customer
from CustomerReg.PO.base_page import BasePage
from CustomerReg.PO.GetVerifyCode import Get_VerifyCode
from CustomerReg.Get_file import Get_File
import  ConfigParser




def NewReg(driver,PhoneNum,PassWord,DistrictcodeFile_Path,Screenshot_path):
    #随机生成客户注册信息
    NewCustomer=Customer()
    IdentifyNum=NewCustomer.Gener_IdentifyNum(DistrictcodeFile_Path)
    CusName=NewCustomer.Gener_CusName()
    CusMail=NewCustomer.Gener_Email(CusName)

    # 在首页点击 我的，进入登录页面，点击注册，进入注册页面
    driver.implicitly_wait(120)
    driver.find_element_by_id('profile_card').click()
    driver.find_element_by_id('tv_register').click()
    driver.find_element_by_id('ll_consumer_user').click()
    driver.find_element_by_id('ll_new_user').click()
    driver.find_element_by_id('layout_inland').click()
    driver.find_element_by_id('edit_phone').send_keys(PhoneNum)
    driver.find_element_by_id('tv_getverify').click()

    # 如果账号未被注册过获取验证码继续完成注册过程
    verify =driver.find_element_by_id('tv_getverify').get_attribute('text')
    if verify != u'获取验证码':
        smsVerify = Get_VerifyCode(PhoneNum)
        print smsVerify
        driver.find_element_by_id('edit_yanzheng').send_keys(smsVerify)
        time.sleep(1)
        driver.find_element_by_id('tv_nextstep').click()
        driver.find_element_by_id('edit_password').send_keys(PassWord)
        driver.find_element_by_id('edit_reinput').send_keys(PassWord)
        time.sleep(2)
        driver.find_element_by_id('tv_nextstep').click()
        time.sleep(1)
        driver.find_element_by_id('tv_hulue').click()
        time.sleep(1)
        #绘制和确认手势密码
        Page=BasePage(driver)
        Page.drawGestureCode()
        Page.drawGestureCode()
        #实名认证
        time.sleep(1)
        driver.find_element_by_id('edit_phone').send_keys(CusName)
        driver.find_element_by_id('edit_yanzheng').send_keys(IdentifyNum)
        driver.find_element_by_id('edit_email').send_keys(CusMail)
        driver.find_element_by_id('tv_nextstep').click()

    # 如果账号已经被注册截图保存报错页面
    else:
        errorPage=BasePage(driver)
        errorPage.screenshot(Screenshot_path)
        driver.find_element_by_id('tb_goBack').click()
        driver.find_element_by_id('tb_goBack').click()
        print u'Error: Register a new account with (' + PhoneNum + ') is failed, and the screenshot has been saved in ' + os.getcwd()



if __name__=='__main__':
    #通过配置文件获取测试数据
    FileList=Get_File('..\Reg_Config')
    DistrictcodeFile_Path=FileList[3]
    Screenshot_path=FileList[5]

    #安装app
    driver=Install_App('..\Reg_Config')

    NewReg(driver, '14477880030', 'qwe123', DistrictcodeFile_Path, Screenshot_path)










