import pymysql
from ddt_data.change_data import mysql_host,mysql_user,mysql_passwd,mysql_db
 
class mySql_use():
    def __init__(self):
        self.ip=mysql_host
        self.user=mysql_user
        self.pwd=mysql_passwd
        self.table_name=mysql_db
    def contect_mysql(self):
        try:  
            self.db = pymysql.connect(self.ip,self.user,self.pwd,self.table_name,charset="utf8")
        except Exception as msg:
            print(u"数据库链接异常%"%msg)
            raise
        else:
            return self.db
        
    def sql_select(self,sql_str):
        self.cursor = self.contect_mysql().cursor()
        self.sql=sql_str
        try:
            # 执行SQL语句
            self.cursor.execute(self.sql)
            #获取所有记录列表
            results = self.cursor.fetchall()
        except Exception as msg:
            #执行异常后回滚
            self.db.rollback()
            print(u'执行查询异常:%s'%msg)
        else:
            return results
        finally:
            #关闭指针对象
            self.cursor.close()
            #关闭连接对象
            self.db.close()
    
    def sql_insert(self,sql_str):
        self.cursor = self.contect_mysql().cursor()
        self.sql=sql_str
        try:
            # 执行SQL语句
            self.cursor.execute(self.sql)
        except Exception as msg:
            self.db.rollback() #执行异常后回滚
            print(u'执行插入异常:%s'%msg)
        else:#commit是和rollback同级别的
            self.db.commit()  #必须提交,在保证执行sql不报错的情况下
        finally:
            #关闭指针对象
            self.cursor.close()
            #关闭连接对象
            self.db.close()
            
if __name__=="__main__":
    mq=mySql_use()
#     mq.sql_insert(sql_str="INSERT INTO sys_config (key_id,key_value,key_group,descs) VALUES ('6003','OFF','6000','自定义')")
#     print(mq.sql_select(sql_str="select * from sys_config where key_id='6003'")[0])
#     sql_str="insert into zoo_question(id,title,context,create_time,status) values ('28','问题6','context内容6','2019-04-23 17:06:40','11')"
    sql_str="UPDATE zoo_orders SET pay_status='21' WHERE id ='145'"
    mq.sql_insert(sql_str)