#coding=utf-8
import ConfigParser
from Basic_oper.Excel_oper import Excel_file
import os

def Get_File(ConfigFile):

    # 通过脚本当前路径拼接其他文件的路径函数
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    cf = ConfigParser.ConfigParser()
    cf.read(ConfigFile)
    # 从外部excel文档读取待注册数据的条数
    RegFile = PATH(cf.get('TestData', 'DataFile_Path'))

    RegSheetName = cf.get('TestData', 'SheetName')
    AccountToReg = Excel_file()
    rows = (AccountToReg.Get_FileInf(RegFile, RegSheetName))[0]
    cols = (AccountToReg.Get_FileInf(RegFile, RegSheetName))[1]

    # 获取bankcode,districtcode文件的路径，生成随机银行卡和身份证号
    # Output_path存放注册完成的账号信息以及注册失败的截图存放路径
    BankCode_filePath = PATH(cf.get('TestFile', 'BankFile'))
    DistrictcodeFile_Path = PATH(cf.get('TestFile', 'DistributeFile'))
    OutPut_path = PATH(cf.get('TestFile', 'OutPutFile'))
    Screenshot_path = PATH(cf.get('TestFile', 'OutPutFile'))

    FileList = [RegFile,RegSheetName, BankCode_filePath, DistrictcodeFile_Path, OutPut_path,Screenshot_path]  # 定义一个列表存放获取的数据信息
    return FileList

if __name__=='__main__':
    Get_File()

