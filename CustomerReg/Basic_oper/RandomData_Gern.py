#coding=utf-8
from appium import webdriver
import string,random
import xlrd
import datetime

class Customer(object):
    #随机生成客户姓名
    def Gener_CusName(self):
        CusName=string.join(random.sample('abcdefghijklmnopqrstuvwxyz',6)).replace(' ','')
        print CusName
        return CusName

    #随机生成邮箱
    def Gener_Email(self,username):
        CusEmail=str((username)+'@'+random.choice(['163.com','quarkfinance.com']))
        print CusEmail
        return CusEmail

    #随机生成银行卡号
    def Gener_Bankno(self, BankCode_filePath):
        f = xlrd.open_workbook(BankCode_filePath)
        # shxrange = range(f.nsheets)
        try:
            sh = f.sheet_by_name("Sheet1")
        except:
            print "no sheet in %s named Sheet1" % fname
        # 获取行数
        nrows = sh.nrows

        row_list = []
        # 获取各行数据
        for i in range(1, nrows):
            row_data = sh.row_values(i)
            row_list.append(row_data)
        # print row_list
        # 随机选择其中一行
        slice = random.choice(row_list)
        BankCode = slice[0] #第一列是银行编码
        # print BankCode

        # 获取第二个元素和第三个元素，计算得出银行卡中间位数
        a1 = int(slice[1])
        a2 = int(slice[2])
        length_bc = int(a1 - a2 - 1)
        # 随机生成除校验码以外数字组合
        str_bank_md = string.join(random.sample('01234567890123456789', length_bc)).replace(" ", "")
        str_bank_front = slice[3] + str_bank_md
        # print str_bank_front
        checkstr = str_bank_front[::-1]
        checkstr1 = checkstr[::2]
        checkstr2 = checkstr[1::2]
        # print checkstr1, checkstr2
        i = 0
        count = 0
        sum1 = 0
        sum2 = 0

        for i in range(len(checkstr1)):
            count = count + int(checkstr1[i:i + 1]) * 2
        # print count
        while count > 0:
            sum1 = sum1 + count % 10
            count = count / 10
        # print sum1
        for i in range(len(checkstr2)):
            sum2 = sum2 + int(checkstr2[i:i + 1])
        # print sum2
        checknum = 10 - (sum1 + sum2) % 10
        # print checknum
        BankNum = str_bank_front + str(checknum)
        print BankNum, BankCode
        return (BankNum, BankCode)


    #随机生成身份证号
    def Gener_IdentifyNum(self,DistrictcodeFile_Path):
        #将distributcode文档中的地区编号按省、市、区放入列表中
        def Getdistrictcode(self, DistrictcodeFile_Path):
            with open(DistrictcodeFile_Path) as file:
                data = file.read()
                districtlist = data.split('\n')

            global codelist
            codelist = []

            for node in districtlist:
                # print node
                if node[10:11] != ' ':
                    state = node[10:].strip()
                if node[10:11] == ' ' and node[12:13] != ' ':
                    city = node[12:].strip()
                if node[10:11] == ' ' and node[12:13] == ' ':
                    district = node[14:].strip()
                    code = node[0:6]
                    codelist.append({"state": state, "city": city, "district": district, "code": code})

        Getdistrictcode(self,DistrictcodeFile_Path)
        id = codelist[random.randint(0, len(codelist))]['code']  # 地区项
        id = id + str(random.randint(1980, 1995))  # 年份项
        da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  # ，顺序号简单处理

        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                     '10': '2'}  # 校验码映射
        for i in range(len(id)):
            count = count + int(id[i:i + 1]) * weight[i]
        id = id + checkcode[str(count % 11)]  # 算出校验码并拼接到id后
        return id




