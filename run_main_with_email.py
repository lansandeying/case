import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
from public.send_email import email_user
import os

if __name__=="__main__":  
    case_path=os.path.join(os.getcwd(),"case")
    report_path=os.path.join(os.getcwd(),"report\htm")
    discover = unittest.defaultTestLoader.discover(case_path,pattern = 'test*.py',top_level_dir=None)
  
  
    #报告时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
      
    #报告名称
    filename = report_path + now + '_test_result.html'   
      
    fp = open(filename,"wb")  
    #定义runner对象 
    runner = HTMLTestRunner(stream =  fp,  
                            title = u"测试报告",  
                            description = u"测试用例执行情况",
                            verbosity=2, #级别2
                            retry=1)   #失败重跑一次
    time.sleep(3)

    #将加载的用例放入run方法  
    runner.run(discover)  
    fp.close() #关闭
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
    x_email.email_body_flie(subject, file_path=filename)
    
    