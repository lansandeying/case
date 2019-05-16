# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标事件
from selenium.webdriver.support.select import Select #导入下拉
# from selenium.common.exceptions import * # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC #导入元素判断
from selenium.webdriver.support.ui import WebDriverWait #导入显示等待
# from selenium.webdriver.common.by import By #导入定位元素By方法
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
class Public_flies():
    def __init__(self,driver):
        self.driver=driver
    
    def open(self,url,text='',timeout=10):
        '''使用get打开URL后，最大化窗口，判断title是否符合预期'''
        self.driver.get(url)
        self.driver.maximize_window()
        title_result=self.get_title_is(text=text)
        if title_result==True:
            log.info(u"标题匹配")
        elif title_result==False:
            log.error(u"标题不匹配")
        else:
            log.error(u"open函数引用异常")
            
    def get_title_is(self,text,timeout=10):
        #用于断言-传text，返回true或false
        try:
            log.info("查看title")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.title_is(text))
        except Exception as msg:
            log.error("title不匹配%s"%msg)
            return False
        else:
            return result 
    
    def get_title_contains(self,text,timeout=10):
        #用于断言-传text，返回true或false
        try:
            log.info("查看title")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.title_contains(text))
        except Exception as msg:
            log.error("title不匹配%s"%msg)
            return False
        else:
            return result 
        
    def get_text_present(self,locator,text,timeout=10):
        #传locator,text，返回true，或返回false（和try组合）
        try:
            log.info("预期元素文本text")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.text_to_be_present_in_element(locator,text))
        except Exception as msg:
            log.error("预期元素文本不匹配或找不到%s"%msg)
            return False
        else:
            return result
        
    def get_value_present(self,locator,value,timeout=10):
        #传locator,value，返回true，或返回false（和try组合）
        try:
            log.info("预期元素文本text")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.text_to_be_present_in_element_value(locator,value))
        except Exception as msg:
            log.error("预期元素文本不匹配或找不到%s"%msg)
            return False
        else:
            return result
        
    def get_element_to_be_selected(self,element,timeout=10):
        try:
            log.info("查看列表勾选结果")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.element_to_be_selected(element))
        except Exception as msg:
            log.error("未勾选%s"%msg)
            return False
        else:
            log.info("确认已勾选")
            return result
        
    def get_element_located_to_be_selected(self,locator,timeout=10):
        try:
            log.info("查看列表勾选结果")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.element_located_to_be_selected(locator))
        except Exception as msg:
            log.error("未勾选%s"%msg)
            return False
        else:
            log.info("确认已勾选")
            return result
        
    def get_element_selection_state_to_be(self,element,state=True,timeout=10):
        try:
            log.info("查看列表勾选结果和预期结果对比")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.element_selection_state_to_be(element,state))
        except Exception as msg:
            log.error("勾选结果和预期结果不匹配%s"%msg)
            return False
        else:
            log.info("确认符合预期")
            return result
        
    def get_element_located_selection_state_to_be(self,locator,state=True,timeout=10):
        try:
            log.info("查看列表勾选结果和预期结果对比")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.element_located_selection_state_to_be(locator,state))
        except Exception as msg:
            log.error("勾选结果和预期结果不匹配%s"%msg)
            return False
        else:
            log.info("确认符合预期")
            return result 
              
    def find_lambda(self,xpath,timeout=10):
        #用于找位置-传xpath路径，返回元素位置
        try:
            log.info("寻找元素")
            result_element=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(lambda x:x.find_element_by_xpath(xpath))
        except Exception as msg:
            log.error("未找到元素%s"%msg)
        else:
            log.info("返回正常元素位置")
            return result_element
        
    def find_element(self,locator,timeout=10):
        #用于找位置-传locator，返回元素位置
        try:
            log.info("寻找元素位置")
            result_element=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.presence_of_element_located(locator))
        except Exception as msg:
            log.error("未找到元素%s"%msg)
        else:
            log.info("返回正常元素位置")
            return result_element      
        
    def find_elements(self,locator,timeout=10):
        #传locator，加载到返回elements的列表，加载不到或返回false（和try组合） 
        try:
            log.info("寻找元素列表位置")
            result_elements=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.presence_of_all_elements_located(locator))
        except Exception as msg:
            log.error("未找到元素列表%s"%msg)
        else:
            log.info("返回正常元素列表位置")
            return result_elements    

    def find_visibility_of_element_located(self,locator,timeout=10):
        #传locator，可见返回element，不可见或返回false（和try组合）
        try:
            log.info("查看元素可见")
            result_element=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.visibility_of_element_located(locator))
        except Exception as msg:
            log.error(u"元素不可见%s"%msg)
            return False
        else:
            log.info("可见并返回位置信息")
            return result_element              

    def find_visibility_of(self,element,timeout=10):
        #传element，可见返回element，不可见或返回false（和try组合）
        try:
            log.info("查看元素可见")
            result_element=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.visibility_of(element))
        except Exception as msg:
            log.error(u"元素不可见%s"%msg)
            return False
        else:
            log.info("可见并返回位置信息")
            return result_element    
        
    def losefind_invisibility_element(self,locator,timeout=10):
        #传locator，不可见返回TRUE，可见返回False（和try组合）
        try:
            log.info(u"判断元素是否可见")
            element=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.invisibility_of_element_located(locator))
        except Exception as msg:
            log.error(u"元素未移除%s"%msg)
            return False
        else:
            log.info(u"元素已移除")
            return element 
   
    def losefind_staleness(self,element,timeout=10):
        # 传element，可见返回false，不可见直接报错（和try组合也有错误）
        try:
            log.info("判断元素是否可见")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.staleness_of(element))
        except Exception as msg:
            log.error(u"元素未移除%s"%msg)
            return False
        else:
            log.info("元素已移除")
            return result

    def is_invisibility(self, locator, timeout=10):
        '''元素可见返回本身，不可见返回 True，没找到元素也返回True'''
        result = WebDriverWait(self.driver, timeout,1).until(EC.invisibility_of_element_located(locator))
        return result   
    def find_iframe(self,frame,timeout=10):
        #传定位到frame的element，找到iframe，且进去返回true；进不去返回False（和try组合）
        try:
            log.info(u"查看且准备进入frame")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.frame_to_be_available_and_switch_to_it(frame))
        except Exception as msg:
            log.error("未找到或没进去frame报错%s"%msg)
            return False #这里的false确保其它错误也有返回值。
        else:
            log.info(u"找到且进入frame")
            return result   
    
    def out_iframe(self): 
        #退出frame窗口  
        self.driver.switch_to.default_content()
             
    def find_alert(self,timeout=10):
        try:
            log.info(u"查看当前页面是否弹出警告框")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.alert_is_present())
        except Exception as msg:
            log.error(u"未发现alert警告框%s"%msg)
            return False
        else:
            log.info(u"发现警告框且切进去")
            return result

    def find_clickable(self,locator,timeout=10):
        #说是可加载出来且可操作才返回element，未发现和visibility有区别       
        #传locator，可见返回element，不可见或返回false（和try组合）
        try:
            log.info(u"查看元素是否找到且可操作")
            result=WebDriverWait(self.driver,timeout=timeout,poll_frequency=1,ignored_exceptions=None).until(EC.element_to_be_clickable(locator))
        except Exception as msg:
            log.error("找不到该元素%s"%msg)
            return False
        else:
            log.info(u"找到该元素且返回位置")
            return result
    
    def find_handles(self,num=1,text=1):
        '''前提，多个页面已打开，句柄列表已形成'''
        #传想要的句柄索引和预期的页面title
        try:
            handle=self.driver.window_handles[num]#默认传第二个句柄，索引为1
            log.info(u"获取指定句柄")
        except Exception as msg:
            log.error(u"没有获取到报错%s"%msg)
        else:    
            self.driver.switch_to.window(handle)
            if self.driver.title==text:
                log.info(u"切换到指定窗口")
            else:
                log.error(u"切换错误")
                
    def move_to_element(self, locator):
        '''
                    鼠标悬停操作
        Usage:
        locator = ("id","xxx")
        driver.move_to_element(locator)
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        
    def get_title(self):
        '''获取title'''
        return self.driver.title
    
    def get_text(self,locator):
        '''获取text文本'''
        element=self.driver.find_element(locator)
        return element.text
    
    def get_attribute(self,locator,name):
        '''获取属性的值'''
        element=self.driver.find_element(locator)
        return element.get_attribute(name)        
        
    def select_by_index(self, locator, index):
        '''通过索引,index 是索引第几个，从 0 开始'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)
    def select_by_value(self, locator, value):
        '''通过 value 属性'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)
    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)
        
    def is_select(self,element):
        #传位置，返回布尔值
        result=element.is_selected()
        return result
    
    def js_element(self):
        
        dict_js={
        "id1" : "document.getElementById('su').click();",
        "name" : "document.getElementsByName('wd')[0].value='selenium';",
        "class_name" : "document.getElementsByClassName('s_btn')[0].click()",
        "css" : "document.querySelectorAll('.s_ipt')[0].value='selenium';",
        "block" : "document.getElementsByClassName('glyphicon')[0].style.display='block';",
        "readonly" : "document.getElementById('train_date').removeAttribute('readonly')" ,
        "body":u"frame内容",
        "frame":'document.getElementById("element_frame").contentWindow.document.body.innerHTML="%s"%body',
        "end": "document.getElementById('su').scrollTop=10000;",
        "top": "document.getElementById('su').scrollTop=0;",
        "right": "document.getElementById('su').scrollLeft=10000;",
        "left": "document.getElementById('su').scrollLeft=0;"}
        return dict_js

    def js_execute(self,js):
        '''执行js'''
        return self.driver.execute_script(js)
    
    def js_focus_element(self,way,key):
        '''聚焦元素'''
        target=self.driver.find_element(way,key)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
        
    def js_scroll_top(self):
        '''滚动到顶部'''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)
        
    def js_scroll_end(self):
        '''滚动到顶部'''
        js="window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js) 
    def click(self,locator):
        '''click和find_element判断元素组合'''
        element=self.find_element(locator=locator)
        element.click()
    def send_keys(self,locator,text):
        '''send_keys和find_element判断元素组合'''
        element=self.find_element(locator=locator)
        element.click()
        element.clear()
        element.send_keys(text)
        