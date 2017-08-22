#coding=utf-8
from selenium import webdriver
import  requests
import re

def Get_VerifyCode(PhoneNum):
    # 创建会话对象requests.Session能够跨请求地保持某些参数，
    # 比如cookies，即在同一个Session实例发出的所有请求都保持同一个cookies
    s = requests.session()
    # 通过接口发送登录信息登录
    url_msg = 'http://qf-coreuat-01:8118/sms-frontal/login'
    payload_login = {'username': 'sms_test', 'password': 'sms_test'}
    headers_login = {
        'Host': 'qf-coreuat-01:8118',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://qf-coreuat-01:8118',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2887.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://qf-coreuat-01:8118/sms-frontal/login',
    }
    r = s.post(url_msg, payload_login, headers_login)
    print r.status_code

    # 通过手机号码查询第一条信息记录，并获取结果json第一行的content值，通过正则表达式取到验证码
    url_query = 'http://qf-coreuat-01:8118/sms-frontal/MessageController/queryMsg'
    payload_query = {'phoneNumber': PhoneNum, 'page': '1', 'rows': '1'}
    headers_query = {
        'Host': 'qf-coreuat-01:8118',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://qf-coreuat-01:8118',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2887.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://qf-coreuat-01:8118/sms-frontal/MessageController/to_messageList',
    }
    r = s.post(url_query, payload_query, headers_query)
    print r.status_code
    sms_content = r.json()['rows'][0]['content']
    print sms_content

    result_sms = re.findall(r'[0-9]{6}', sms_content)
    print result_sms
    return result_sms


if __name__ == '__main__':
    sms_verify = Get_VerifyCode('15618275251')

