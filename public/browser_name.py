# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from public import log_out
log=log_out.logger()

hub_path="http://192.168.0.75:4444/wd/hub"
def browser(browser='firefox'):
    """
        打开浏览器凼数，"firefox"、 "chrome"、 "ie"、 "phantomjs"
    """
    try:
        if  browser == "firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "chrome":
            driver = webdriver.Chrome()
            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
            return driver
        elif browser == "firefoxpath":
            #配置文件地址
            profile_directory=r"C:\Users\hp\AppData\Roaming\Mozilla\Firefox\Profiles\wwkp7eh1.default"
            #加载配置
            profile=webdriver.FirefoxProfile(profile_directory)
            #启动浏览器配置
            driver=webdriver.Firefox(profile)
            return driver
        elif browser == "chromepath":#前提，没有谷歌浏览器打开
            # 个人资料路径
            user_data_dir = r'--user-data-dir=C:\Users\hp\AppData\Local\Google\Chrome\User Data'#\Default
            # 加载配置数据
            option = webdriver.ChromeOptions()
            option.add_argument(user_data_dir)
            # 启动浏览器配置
            driver = webdriver.Chrome(chrome_options=option, executable_path=r'C:\chomedriver\chromedriver.exe')
            return driver
        elif browser=="firefox_grid1":
            capabilities = DesiredCapabilities.FIREFOX
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "firefox"
            driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
            return driver
        elif browser=="chrome_grid2":
            capabilities = DesiredCapabilities.CHROME
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "chrome"  
            driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
            return driver       
        elif browser=="internet_explorer_grid1":
            capabilities = DesiredCapabilities.INTERNETEXPLORER
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "internet explorer"
            driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
            return driver
        elif browser=="firefox_grid2":
            capabilities = DesiredCapabilities.FIREFOX
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "firefox"   
            capabilities["version"] = "version"  #待写入  
        elif browser=="chrome_grid2":
            capabilities = DesiredCapabilities.CHROME
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "chrome"   
            capabilities["version"] = "version" #待写入
            driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
            return driver
        elif browser=="internet_explorer_grid2":
            capabilities = DesiredCapabilities.INTERNETEXPLORER
            capabilities["platform"] = "ANY" 
            capabilities["browserName"] = "internet explorer"   
            capabilities["version"] = "version" #待写入  
            driver= webdriver.Remote(command_executor=hub_path, desired_capabilities=capabilities )
            return driver 
        else:
            print("Not found this browser,You can enter 'firefox','chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        log.error ("%s" % msg)