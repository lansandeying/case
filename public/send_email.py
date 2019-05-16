#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.log_out import logger
import time
log=logger()
now = time.strftime("%Y-%m-%d %H-%M-%S")
 
class email_user():
    def __init__(self,sender,psw,receiver,way="163"):
        self.sender=sender
        self.psw=psw
        self.receiver=receiver
        self.way=way
        if self.way=="163":
            self.smtpserver="smtp.163.com"       #发件服务器
            self.port=0                          #端口
        elif self.way=="QQ":
            self.smtpserver="smtp.qq.com"        #发件服务器
            self.port=465                        #端口            
        else:
            log.error(u"传值错误,没有该类型邮箱")
    def email_body(self,subject,body,decode="html"):

            
        #------------2:编辑邮件的内容------------
        self.subject=now+subject             #邮件标题
        self.body=body                       #定义邮件正文为HTML格式,内容
        self.decode=decode
 
        msg=MIMEText(body,self.decode,"utf-8")  #将邮件内容打包定义为实例对象
        msg['from']=self.sender   #将信息装入实例对象包
        msg['to']=",".join(self.receiver)
        msg['subject']=self.subject
        
 
        #------------3:发送邮件-----------------
 
        try:
            log.info(u"调用163")
            smtp=smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.sender, self.psw)
        except:
            log.info(u"调用QQ")
            smtp=smtplib.SMTP_SSL(self.smtpserver,self.port)
            smtp.login(self.sender,self.psw)
        smtp.sendmail(self.sender,msg['to'].split(','),msg.as_string())
        smtp.quit()
        
    def email_body_flie(self,subject,file_path):
        self.subject=now+subject
        self.file_path=file_path
        with open(self.file_path,"rb") as fp:
            mail_body=fp.read()
     
        msg=MIMEMultipart()
        msg["from"]=self.sender
        msg["to"]=",".join(self.receiver)
        msg["subject"]=self.subject
 
        #正文    
        body=MIMEText(mail_body,"html","utf-8")
        msg.attach(body)
 
        #附件
        att=MIMEText(mail_body,"base64","utf-8")
        att["Content-Type"]="application/octet-stream"
        att["Content-Disposition"]='attachment;filename=test_report.html'
        msg.attach(att)
        #------------3:发送邮件-----------------
 
        try:
            log.info(u"调用163")
            smtp=smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.sender, self.psw)
        except:
            log.info(u"调用QQ")
            smtp=smtplib.SMTP_SSL(self.smtpserver,self.port)
            smtp.login(self.sender,self.psw)
        smtp.sendmail(self.sender,msg['to'].split(','),msg.as_string())
        smtp.quit()
if __name__=="__main__":
    sender="516015922@qq.com"
    psw="opvibqkkinnkcaai"
    receiver=["452949134@qq.com","18033084759@163.com"]
    print(receiver)
    way="QQ"
    x_email=email_user(sender,psw,receiver,way)
    subject=u"测试报告"
#     body=u"测试结果报告展示"
#     decode="plain"
#     x_email.email_body(subject, body, decode)
    filename=r"C:\Users\hp\eclipse-workspace\test_blog\report\htm2019-02-25 10-20-01_test_result.html"
    x_email.email_body_flie(subject, file_path=filename)