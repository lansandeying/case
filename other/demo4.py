import unittest
import time 
from tomorrow import threads
from selenium import webdriver

class Test_Thread(unittest.TestCase):
    def setUp(self):
        self.list=["http://www.baidu.com","http://ac.qq.com","http://www.u17.com"]        
    def tearDown(self): 
        print("end test")         
    def testBaidu1(self):
        start = time.time()
        for i in self.list: 
            self.driver=webdriver.Chrome()  
            @threads(5)
            def baidu(driver,num): 
                driver=driver
                driver.get(num)
                time.sleep(3)
                driver.quit() 
            baidu(self.driver,num=i)
        end=time.time()
        print("Time: %f seconds" % (end - start))  
if __name__=="__main__":
#     unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(Test_Thread("testBaidu1")) #类名+case名
    runner=unittest.TextTestRunner()
    runner.run(suite)