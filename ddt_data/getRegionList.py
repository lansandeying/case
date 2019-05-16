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

#获取地理位置接口
class getRegionList():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_RegionList=host+port+r'/region/getRegionList'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        
        self.payload1={"id":"0"}
        self.payload2={"id":"440000"}
        self.payload3={"id":"440300"}
        
        self.list_data=[{'canshu':self.payload1,'code':'0000','have':u'河北省'},
                        {'canshu':self.payload2,'code':'0000','have':u'深圳市'},
                        {'canshu':self.payload3,'code':'0000','have':u'南山区'}
                        ]
        
    def get_region_true(self,data):
        
        try:
            log.info(u"执行查询region操作")
            r=self.sr.get(url=self.url_RegionList,headers=self.header_suc,params=data)
        except Exception as msg:
            log.error(u"执行查询region操作报错%s"%msg)
            raise
        else:
            return r.json()
        
if __name__=="__main__":
    sr=requests
    r=getRegionList(sr)
#     print(q.header_suc)
#     print(q.match_id())
    print(r.get_region_true())
    
    
    