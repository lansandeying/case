#未完成，待补全
import requests
#获取具体的请求host和port
from ddt_data.change_data import host,port
#获取登录类
from ddt_data.sys_login_action import get_login
#获取日志对象
from public.log_out import logger
log=logger()
#获取数据库对象
from public.mysql_sql import get_mysql_data
sql="select * from zoo_question order by id desc limit 1"
mql=get_mysql_data(sql)
re_mql=mql['id'][0]
#拿到实时时间
import time
now = time.strftime("%Y-%m-%d %H:%M:%S")

class question_insert():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_question_insert=host+port+r'/question/insert'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        #token值为空
        self.header1={"Accept": "*/*","token": "","Content-Type": "application/json"}
        #token值错误
        self.header2={"Accept": "*/*","token": "111111111","Content-Type": "application/json"}
        #token参数为空
        self.header3={"Accept": "*/*","": self.token,"Content-Type": "application/json"}
        #token参数错误
        self.header4={"Accept": "*/*","tokenfalse": self.token,"Content-Type": "application/json"}

        self.list_header=[{"canshu":self.header1,"code":"","msg":"","descript":u"token值为空"},
                     {"canshu":self.header2,"code":"","msg":"","descript":u"token值错误"},
                     {"canshu":self.header3,"code":"","msg":"","descript":u"token参数为空"},
                     {"canshu":self.header4,"code":"","msg":"","descript":u"token参数错误"}
                     ]
        
        self.data_suc={
            "context": u"context4511",
            "createTime": "",
            "id": "",
            "remark": u"remark4511",
            "status": "Y1ES",
            "title": u"title4511",
            "updateTime": ""
            }
        #{"context": "context内容","createTime": now,"id": re_mql+1,"remark": "","status": "YES","title": "问题","updateTime": ""}
        #内容数据不能为空
        self.data1={"context": u"","createTime": now,"id": re_mql+1,"remark": "","status": "YES","title": u"问题","updateTime": ""}
        #创建时间格式异常
        self.data2={"context": u"context内容","createTime": "2019-04-23 17-06-40","id": re_mql+1,"remark": "","status": "YES","title": u"问题","updateTime": ""}
        #创建时间可以为空
        self.data3={"context": u"context内容","createTime": "","id": re_mql+1,"remark": "","status": "YES","title": u"问题","updateTime": ""}
        #id可以覆盖，覆盖时，必须传updatetime，createtime不用传
        self.data4={"context": u"改动过的内容","createTime": "","id": 5,"remark": "","status": "YES","title": u"改动过得标题","updateTime": now}
        #id不能为空
        self.data5={"context": "context内容","createTime": now,"id": "","remark": "","status": "YES","title": "问题","updateTime": ""}
        
        
        self.list_data=[  {"canshu":self.data1,"code":"","msg":"","descript":u"token值为空"},
                     {"canshu":self.data2,"code":"","msg":"","descript":u"token值错误"},
                     {"canshu":self.data3,"code":"","msg":"","descript":u"token参数为空"},
                     {"canshu":self.data4,"code":"","msg":"","descript":u"token参数错误"}
                     ]
        
    def question_insert_true(self):
        try:
            log.info(u"question插入接口为true请求开始")
            r=self.sr.post(url=self.url_question_insert,headers=self.header_suc,json=self.data_suc)
        except Exception as msg:
            log.error(u"question插入接口为true请求报错%s"%msg)
        else:
            return r.json()         
    
    def question_insert_header_false(self,header):     
        try:
            log.info(u"question插入接口header为false请求开始")
            r=self.sr.post(url=self.url_question_insert,headers=header,json=self.data_suc)
        except Exception as msg:
            log.error(u"question插入接口header为false请求报错%s"%msg)
        else:
            return r.json()    
        
    def question_insert_body_false(self,data):
        try:
            log.info(u"question插入接口body为false请求开始")
            r=self.sr.post(url=self.url_question_insert,headers=self.header_suc,json=data)
        except Exception as msg:
            log.error(u"question插入接口body为false请求报错%s"%msg)
        else:
            return r.json()  
        
if __name__=="__main__":
#     print(re_mql+1)
#     print(now)
    sr=requests
    q=question_insert(sr)
#   正确请求 
    print(q.question_insert_true())

#header失败请求
#     list=q.list_header
#     for i in range(0,4):
#         print(list[i]['canshu'])
#         print(q.question_insert_header_false(list[i]['canshu']))
#         print("")
#         time.sleep(1)
         
        
        