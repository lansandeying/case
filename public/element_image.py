#coding:utf-8
from PIL import Image
from selenium import webdriver
from public.log_out import logger
log=logger()

def element_PIL_Image(driver,image_path,element):
    
    try:
        #最左端的坐标大小为
        left=element.location["x"]
        #最上端的坐标大小为
        top=element.location["y"]
        #最右端的坐标大小为
        right=element.location["x"]+element.size["width"]
        #最底端的坐标大小为
        bottom=element.location["y"]+element.size["height"]
        #定义要保存图片的名称及格式
        driver.save_screenshot(image_path)
        #打开图片文件
        im=Image.open(image_path)
        #截取图片坐标
        im=im.crop((left,top,right,bottom))
        #截取图片后保存至图片文件内
        im.save(image_path)
    except Exception as msg:
        log.error(u"未保存成功%s"%msg)
        return False
    else:
        return True    
    
if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    image_path=r"D:\button3.png"
    element=driver.find_element("link text",u"新闻")
    element_PIL_Image(driver, image_path, element)    