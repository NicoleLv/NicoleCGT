import  ConfigParser
import  os

PATH= lambda p :os.path.abspath(os.path.join(os.path.dirname(__file__),p))
print PATH('UFO_apk\ufo.apk')
cf=ConfigParser.ConfigParser()
cf.read('Reg_Config')
print cf.sections()
print cf.get('TestData','DataFile_Path')
print cf.get('AppInf','platformName')
print cf.get('AppInf','app')