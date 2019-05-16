from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def browser_data(browser_name="normal"):
    if browser_name=="normal":
        browser=["ie","firefox","chrome"]
        
        return browser      
    elif  browser_name=="seleniumgrid":      
        browser=[{"browser":"chrome","platform":"ANY","version":None},{"browser":"firefox","platform":"ANY","version":None}]
        return browser
    else:
        print(u"传浏览器并发类型错误")