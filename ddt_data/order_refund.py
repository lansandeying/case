#未完成，待补全
import requests
#获取具体的请求host和port
from ddt_data.change_data import host,port,order_refund_num,order_refund_sql,order_update_sql
#获取登录类
from ddt_data.sys_login_action import get_login
#获取日志对象
from public.log_out import logger
log=logger()

#获取插入数据库对象
from public.mysql_insert import mySql_use

#拿到实时时间
import time
now = time.strftime("%Y-%m-%d %H:%M:%S")


class orderRefund():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
#         self.url_order_refund=host+port+r'/order/refund/%s'%order_refund_num
        self.url_order_refund=host+port+r'/order/refund/150'
  
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        
        self.payload={}
        
    #插入一条数据，有则回退    
    def change_paystatus(self):
        log.info(u"插入order表数据")
        sql_str=order_refund_sql
        mql=mySql_use()
        mql.sql_insert(sql_str)
        
        log.info(u"更新order表数据")
        sql_str_update=order_update_sql
        mql.sql_insert(sql_str_update)
        
    def get_order_refund_true(self):
        try:
            log.info(u"执行查询order_refund操作")
            r=self.sr.post(url=self.url_order_refund,headers=self.header_suc,params=self.payload)
        except Exception as msg:
            log.error(u"执行查询order_refund操作报错%s"%msg)
        else:
            return r.json()
        
if __name__=="__main__":
    sr=requests
    o=orderRefund(sr)
    print(o.url_order_refund)
    print(o.get_order_refund_true())
    
    