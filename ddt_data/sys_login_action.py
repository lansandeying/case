import requests

from public.log_out import logger
log=logger()

from ddt_data.change_data import host,port

import time


class get_login():        
    url_login=host+port+r'/sys/login'
    
    header={
      "Accept": "*/*",
      "Content-Type": "application/json"
    }

    data_suc_login={"username":"admin","password":"123456"}
    def post_login_s(self):
        try:
            log.info("发起登录请求")
            print()
            r=self.sr.post(url=self.url_login,headers=self.header,json=self.data_suc_login)
        except Exception as msg:
            log.error("登录成功请求报错：%s"%msg)
            raise          
        else:
            return r.json()

    data1={"username":"admin1","password":"123456"}
    data2={"username":"admin","password":"1234567"}
    data3={"username":"","password":"123456"}
    data4={"username":"admin","password":""}
    data5={"username":"","password":""}
    data6={"user":"admin","password":"123456"}
    data7={"username":"admin","passwd":"123456"}
    data8={"":"admin","password":"123456"}
    data9={"username":"admin","":"123456"}
    data10={"":"admin","":"123456"}

    list_data=[{"canshu":data1,"code":'501',"msg":u"账号或密码不正确","code":'501'},
               {"canshu":data2,"code":'501',"msg":u"账号或密码不正确","code":'501'},
               {"canshu":data3,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data4,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data5,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data6,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data7,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data8,"code":'501',"msg":u"请求参数为空","code":'1000'},
               {"canshu":data9,"code":'501',"msg":u"请求参数为空","code":'1000'}
               ]
    
    def __init__(self,sr):
        self.sr=sr           



    def post_login_f(self,data):
        try:
            log.info("发起登录失败请求")
            print()
            r=self.sr.post(url=self.url_login,headers=self.header,json=data['canshu'])
        except Exception as msg:
            log.error("登录失败请求报错：%s"%msg)
            raise          
        else:
            return r.json()
    
    def get_token(self):
        try:
            log.info("发起登录成功请求")
            print()
            r=self.sr.post(url=self.url_login,headers=self.header,json=self.data_suc_login)
        except Exception as msg:
            log.error("登录成功请求报错：%s"%msg)
            raise          
        else:
            return r.json()['token']

if __name__=="__main__":
    sr=requests
    login=get_login(sr)
#     print(login.post_login_s())
    print(login.get_token())
#     data=login.list_data
#     for i in range(0,9):
#         print(data[i]['canshu'])
#         print(login.post_login_f(data[i]['canshu']))
#         time.sleep(1)
#         print("")
#         print("")
    