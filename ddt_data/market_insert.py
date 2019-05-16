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

class market_Insert():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_market_insert=host+port+r'/info/insert'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
        }
        
        self.data={
            "createTime": "",
            "id": "",
            "isDel": "YES",
            "remark": u"备注1100",
            "updateTime": "",
            "zooAddress": u"动物园地址",
            "zooIntroduce": u"描述1",
           # "zooLatitude": "22.528499",  #纬度
           #"zooLongitude": "113.923552", #经度
            "zooName": "动物园名称1101",
            "zooRegion": "广东省 深圳市 南山区",
            "zooRegionId": "440300",#动物园区域
            "zooStatus": "UpperShelf" #只接收UpperShelf, LowerShelf
        }
              
    def get_market_insert_true(self):
        try:
            log.info(u"执行market_insert操作")
            r=self.sr.post(url=self.url_market_insert,headers=self.header_suc,json=self.data)
        except Exception as msg:
            log.error(u"执行market_insert操作报错%s"%msg)
        else:
            return r.json()
        
if __name__=="__main__":
    sr=requests
    m=market_Insert(sr)
    print(m.get_market_insert_true())