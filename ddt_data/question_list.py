import requests
from ddt_data.change_data import host,port
from ddt_data.sys_login_action import get_login
from public.log_out import logger
log=logger()
import time
now = time.strftime("%Y-%m-%d %H-%M-%S")
class question_list():
        
    def __init__(self,sr):
        self.sr=sr  
        self.token=get_login(self.sr).get_token()
    
        self.url_question_list=host+port+r'/question/getQuestionList'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
    
        self.header1={"Accept": "*/*","token": "","Content-Type": "application/json"}
        self.header2={"Accept": "*/*","token": "111111111","Content-Type": "application/json"}
        self.header3={"Accept": "*/*","token": self.token,"Content-Type": ""}
        self.header4={"Accept": "*/*","token": self.token,"Content-Type": "application/x-www-form-urlencoded"}
        self.header5={"": "*/*","token": self.token,"Content-Type": "application/json"}
        self.header6={"Accept": "*/*","": self.token,"Content-Type": "application/json"}
        self.header7={"Accept": "*/*","token": self.token,"": "application/json"}
        self.header8={"Acceptfalse": "*/*","token": self.token,"Content-Type": "application/json"}
        self.header9={"Accept": "*/*","tokenfalse": self.token,"Content-Type": "application/json"}
        self.header10={"Accept": "*/*","token": self.token,"Content-Typefalse": "application/json"}
        

        self.list_handers=[{"canshu":self.header1,"code":"","msg":""},
                           {"canshu":self.header2,"code":"","msg":""},
                           {"canshu":self.header3,"code":"","msg":""},
                           {"canshu":self.header4,"code":"","msg":""},
                           {"canshu":self.header5,"code":"","msg":""},
                           {"canshu":self.header6,"code":"","msg":""},
                           {"canshu":self.header7,"code":"","msg":""},
                           {"canshu":self.header8,"code":"","msg":""},
                           {"canshu":self.header9,"code":"","msg":""},
                           {"canshu":self.header10,"code":"","msg":""},
                           ]
        
        self.payload={"pageNum":"1",
                      "pageSize":"50",
                      "title":u"",
                      "status":""
                      }
    
    def question_list_true(self):
        try:
            log.info("发起问题列表true查询请求")
            r=self.sr.get(url=self.url_question_list,headers=self.header_suc,params=self.payload)
        except Exception as msg:
            log.error("查询问题列表true请求报错%s"%msg)
            raise
        else:
            return r.json()

    def question_list_header_false(self,header):
        try:
            log.info("发起问题列表查询headerfalse请求")
            r=self.sr.get(url=self.url_question_list,headers=header,params=self.payload)
        except Exception as msg:
            log.error("查询问题列表headerfalse请求报错%s"%msg)
#             raise
        else:
            return r.json()
    
if __name__=="__main__":
    sr=requests
    t=question_list(sr)
    print(t.question_list_true())
    
#     for i in range(0,10):
#         print(i)
#         print(list[i]['canshu'])
#         print(t.question_list_header_false(list[i]['canshu']))
#         print("")
#         sleep(1)
    