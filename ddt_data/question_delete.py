#未完成，待补全
import requests
#获取具体的请求host和port
from ddt_data.change_data import host,port,question_delete_sql,que_num
#获取登录类
from ddt_data.sys_login_action import get_login
#获取日志对象
from public.log_out import logger
log=logger()
#获取数据库对象
from public.mysql_sql import get_mysql_data
#获取插入数据库对象
from public.mysql_insert import mySql_use

#拿到实时时间
import time
now = time.strftime("%Y-%m-%d %H:%M:%S")


class question_delete():
        
    def __init__(self,sr):
        self.sr=sr  
        #根据登录类拿到实时的token
        self.token=get_login(self.sr).get_token()
        #接口请求地址    
        self.url_question_delete=host+port+r'/question/delete/96' #%s'%que_num
    
        self.header_suc={
            "Accept": "*/*",
            "token": self.token,
            "Content-Type": "application/json"
            }
        
        self.payload={}
    
    #插入一条数据，有则回退    
    def insert_id(self):
        log.info(u"插入question表数据")
        sql_str=question_delete_sql
        mql=mySql_use()
        mql.sql_insert(sql_str)
        
    #验证记录已经被删除
    def match_id(self):
        try:
            sql="select * from zoo_question where id = %s"%que_num
        except Exception as msg:
            log.error("校验删除的ID不存在报错%s"%msg)      
        else:
            mql2=get_mysql_data(sql)
            a=str(mql2)
#             print(a)
            if "Empty DataFrame" in a:
                return True
            else:
                log.info("删除失败")
                return False
    
    def question_delete_true(self):
        
        try:
            log.info(u"执行删除question操作")
            r=self.sr.get(url=self.url_question_delete,headers=self.header_suc,params=self.payload)
        except Exception as msg:
            log.error(u"执行删除question操作报错%s"%msg)
        else:
            return r.json()
        

if __name__=="__main__":
    sr=requests
    q=question_delete(sr)
#     print(q.header_suc)
#     print(q.match_id())
    print(q.url_question_delete)
    print(q.question_delete_true())
            
    