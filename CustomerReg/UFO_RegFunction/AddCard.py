#coding=utf-8
from CustomerReg.Basic_oper.RandomData_Gern import Customer
from appium import webdriver
import  time
from CustomerReg.PO.base_page import BasePage
from CustomerReg.PO.GetVerifyCode import Get_VerifyCode
from CustomerReg.Get_file import Get_File
from CustomerReg.Open_App import Install_App


class AddBankCard(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def Add_BankCard(self,Bank_Code,BankNum,UserName,PhoneNum):
        # 从“我的”页面，点击银行卡进入绑卡页面

        self.driver.find_element_by_id('re_bankcard').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('tb_right').click()
        # 输入绑卡信息
        self.driver.find_element_by_id('edit_user_pass').send_keys(UserName)
        self.driver.find_element_by_id('tv_bankname').click()
        time.sleep(2)
        BankCode_list1 = ('GDB', 'COMM', 'SZPAB')
        BankCode_list2 = ('CIB', 'CMB', 'ICBC', 'CEB', 'CCB','CMBC','ABC','BOC')

        # 选择银行
        if Bank_Code in BankCode_list1:
            BankList1 = self.driver.find_elements_by_id('tv_bankname')
            for i in range(3):
                if Bank_Code ==BankCode_list1[i]:
                    BankList1[i].click()
                else:
                    continue
        elif Bank_Code in BankCode_list2:

            self.driver.swipeUp(500)
            time.sleep(2)
            BankList2 = self.driver.find_elements_by_id('tv_bankname')
            time.sleep(2)
            print 'In the BankCode_List2'

            for i in range(8):
                if Bank_Code == BankCode_list2[i]:
                    # 向上滑动之后，第二个页面跟第一个页面有1个银行卡重复，也就是第二页面的第二个银行对应，bankcode的第一个值
                    BankList2[i + 1].click()
                    print 'Bank selected'
                else:
                    continue

        # 输入银行卡卡号
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('edit_cradnum').send_keys(BankNum)
        self.driver.find_element_by_id('edit_phone_num').send_keys(PhoneNum)
        self.driver.find_element_by_id('tv_getverify').click()
        VerifyCode = Get_VerifyCode(PhoneNum)
        self.driver.find_element_by_id('edit_yanzheng').send_keys(VerifyCode)
        self.driver.find_element_by_id('tv_nextstep').click()

#单独给客户绑定一张卡
if __name__=='__main__':
    #获取bankcode存放目录
    FileList=Get_File('..\Reg_Config')
    BankCode_FilePath=FileList[2]
    #随机生成银行卡和银行卡号
    User=Customer()
    BankInfo_List=User.Gener_Bankno(BankCode_FilePath)
    BankNum=BankInfo_List[0]
    Bank_Code=BankInfo_List[1]

    #打开app
    driver = Install_App('..\Reg_Config')
    #客户登录
    driver.implicitly_wait(120)
    driver.find_element_by_id('profile_card').click()
    driver.find_element_by_id('edit_name').send_keys('14477880027')
    driver.find_element_by_id('edit_password').send_keys('qwe123')
    driver.find_element_by_id('tv_login').click()
    time.sleep(1)
    driver.find_element_by_id('profile_card').click()#任意点击激活首页
    driver.find_element_by_id('profile_card').click()#从首页进入我的页面
    driver.find_element_by_id('tv_know').click()



    #添加银行卡
    BankCard=AddBankCard(driver)
    BankCard.Add_BankCard(Bank_Code,BankNum,'rutcxz','14477880027')








