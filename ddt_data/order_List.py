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


class orderList():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_order_list=host+port+r'/order/list'
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        
        self.payload={
            "userId":"",
            "pageNum":"1",
            "pageSize":"60",
            "orderItem":"",
            "goodsName":"",
            "status":"Closed" #All/ToPay/InPay/ToDelivery/Already/PendingRefund/Refund/Refunded/Closed
            }
        
        
    def get_order_list_true(self):
        try:
            log.info(u"执行查询order_list操作")
            r=self.sr.get(url=self.url_order_list,headers=self.header_suc,params=self.payload)
        except Exception as msg:
            log.error(u"执行查询order_list操作报错%s"%msg)
        else:
            return r.json()
        
if __name__=="__main__":
    sr=requests
    o=orderList(sr)
    print(o.get_order_list_true())
    