#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from public.log_out import logger
log=logger()

class seleniumgird_driver():
    def node_used(self,hub_path,browser="firefox",platform="ANY",version=None):
        if browser=="firefox" and platform=="ANY" and version==None:
            capabilities = DesiredCapabilities.FIREFOX
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "firefox"
        elif browser=="chrome" and platform=="ANY" and version==None:
            capabilities = DesiredCapabilities.CHROME
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "chrome"         
        elif browser=="internet explorer" and platform=="ANY" and version==None:
            capabilities = DesiredCapabilities.INTERNETEXPLORER
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "internet explorer"
        elif browser=="firefox" and platform=="ANY" and version != None:
            capabilities = DesiredCapabilities.FIREFOX
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "firefox"   
            capabilities["version"] = version  
        elif browser=="chrome" and platform=="ANY" and version!=None:
            capabilities = DesiredCapabilities.CHROME
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "chrome"   
            capabilities["version"] = version 
        elif browser=="internet explorer" and platform=="ANY" and version!=None:
            capabilities = DesiredCapabilities.INTERNETEXPLORER
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "internet explorer"   
            capabilities["version"] = version   
        else:
            log.info("没有匹配浏览器驱动driver") 
        self.driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
        
        return self.driver                   

if __name__=="__main__":
#     hub_path="http://192.168.0.75:4444/wd/hub"
#     browser="chrome"
#     platform="ANY"
#     version=None
#     driver=seleniumgird_driver().node_used(hub_path=hub_path, browser=browser, platform=platform, version=version)
    hub_path="http://192.168.0.75:4444/wd/hub"
    list_browser=[{"browser":"chrome","platform":"ANY","version":None},{"browser":"firefox","platform":"ANY","version":None}]
    for i in list_browser:
        driver=seleniumgird_driver().node_used(hub_path=hub_path, browser=i["browser"], platform=i["platform"], version=i["version"])
        driver.get("https://www.baidu.com")
 
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
 
        time.sleep(5)
        driver.quit()