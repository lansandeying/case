#coding:utf-8
import unittest   
from HTMLTestRunner_cn import HTMLTestRunner 
import time 
from tomorrow import threads
# from public.send_email import email_user
# from test_mybags import MyTestlogin
@threads(5)  
def run_case(discover,case_path): 
    #文档时间 
    now = time.strftime("%Y-%m-%d %H-%M-%S")  
      
    #文档路径 
    filename = r"F:\my_job\zVke\report\htm" + now  + case_path + '_test_result.html'  
      
    fp = open(filename,"wb")  
    #定义runner对象 
    runner = HTMLTestRunner(stream =  fp,  
                            title = u"测试报告",  
                            description = u"测试用例执行情况",
                            verbosity=2, #级别2执行
                            retry=1)   #失败重跑
    time.sleep(3)

    #加载用例且执行
    runner.run(discover)  
    fp.close() #关闭文件


  
if __name__=="__main__": 
    chrome_path="F:\my_job\zVke\case_chrome"
    firefox_path='F:\my_job\zVke\case_firefox'
    test_dirs = [chrome_path,firefox_path]
    
    for test_dir in test_dirs:
        print(test_dir)
        case_path=test_dir.split('\\')[-1]
        
        unittest.defaultTestLoader._top_level = None
        discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py')
        print(case_path)
#         run_case(discover,case_path)      