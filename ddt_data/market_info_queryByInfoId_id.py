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

class market_QueryById():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_market_query_by_id=host+port+r'/info/queryByInfoId/3'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
        }
        
        self.payload={}
              
    def get_market_query_by_id_true(self):
        try:
            log.info(u"执行market_queryAllInfo操作")
            r=self.sr.get(url=self.url_market_query_by_id,headers=self.header_suc,params=self.payload)
        except Exception as msg:
            log.error(u"执行market_queryAllInfo操作报错%s"%msg)
        else:
            return r.json()
        
if __name__=="__main__":
    sr=requests
    m=market_QueryById(sr)
    print(m.url_market_query_by_id)
    print(m.get_market_query_by_id_true())