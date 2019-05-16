import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
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
                            verbosity=2, #执行级别
                            retry=1)     #失败重跑
    time.sleep(3)
  
    #加载用例至run方法  
    runner.run(discover)  
#     fp.close() #关闭文档