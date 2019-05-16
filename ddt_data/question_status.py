#未完成，待补全
import requests
#获取具体的请求host和port
from ddt_data.change_data import host,port
#获取登录类
from ddt_data.sys_login_action import get_login
#获取日志对象
from public.log_out import logger
log=logger()

#拿到实时时间
import time
now = time.strftime("%Y-%m-%d %H:%M:%S")


class question_Status():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url=host+port+r'/question/updateQuestionStatusList' #%s'%que_num
    
        self.header={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        
        self.data={
            "id":"95",
            "status":"" #UpperShelf  LowerShelf
            }
    
    
    def post_question_status_true(self):
        
        try:
            log.info(u"执行question_status操作")
            r=self.sr.post(url=self.url,headers=self.header,json=self.data)
        except Exception as msg:
            log.error(u"执行question_status操作报错%s"%msg)
        else:
            return r.json()
        

if __name__=="__main__":
    sr=requests
    q=question_Status(sr)
    print(q.post_question_status_true())
            
    