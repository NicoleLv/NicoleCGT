import  ConfigParser
from  Basic_oper.Excel_oper import Excel_file
import  os

PATH= lambda p :os.path.abspath(os.path.join(os.path.dirname(__file__),p))
print PATH('UFO_apk\ufo.apk')
cf=ConfigParser.ConfigParser()
cf.read('Reg_Config')
RegFile=cf.get('TestData','DataFile_Path')
RegSheetName=cf.get('TestData','SheetName')
AccountToReg=Excel_file()
rows=(AccountToReg.Get_FileInf(RegFile,RegSheetName))[0]
cols=(AccountToReg.Get_FileInf(RegFile,RegSheetName))[1]
print rows,cols
TestData_Table=AccountToReg.open_Excel(RegFile).sheet_by_name(RegSheetName)
CusType=TestData_Table.cell(1,0).value
PhoneNum=str(TestData_Table.cell(1,1).value)
PassWord=TestData_Table.cell(1,2).value
print CusType,PhoneNum,PassWord