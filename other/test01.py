import unittest
import time 
from public.public_file import browser
from public.seleniumgird_get import seleniumgird_driver
from tomorrow import threads
from public.data_get import browser_data

class Test_Thread(unittest.TestCase):
    def setUp(self):
        self.hub_path="http://192.168.0.75:4444/wd/hub"
        self.list_browser=browser_data(browser_name="normal")          
    def tearDown(self): 
        print("end test")  
    def testBaidu1(self):
        start = time.time()
        for i in self.list_browser:
#             self.driver=seleniumgird_driver().node_used(hub_path=self.hub_path, browser=i["browser"], platform=i["platform"], version=i["version"])
            self.driver= browser(i)
            @threads(5)   
            
            def baidu1(driver):         
                driver.get("http://www.baidu.com")
                print(driver.title)
                title=driver.title
                re_title=u"百度一下，你就知道"
                self.assertEqual(title, re_title, msg=u"不匹配")
                time.sleep(5)
                driver.quit()
            baidu1(driver=self.driver)
        end=time.time()
        print("Time: %f seconds" % (end - start))   
        
if __name__=="__main__":
    unittest.main()
