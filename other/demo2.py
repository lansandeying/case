import unittest
import time 
from tomorrow import threads
from selenium import webdriver
@threads(5) 
def baidu(driver,num):
    driver=driver
    driver.get(num)
    driver.time.sleep(10)
    driver.quit() 


class Test_Thread(unittest.TestCase):
    def setUp(self):
        self.list=["http://www.baidu.com","http://www.baidu.com","http://www.baidu.com"]        
    def tearDown(self): 
        print("end test")
     

          
    def testBaidu1(self):
        start = time.time()
        for i in self.list: 
            self.driver=webdriver.Chrome()   
            baidu(driver=self.driver,num=i)
        end=time.time()
        print("Time: %f seconds" % (end - start))   
if __name__=="__main__":
    unittest.main()
