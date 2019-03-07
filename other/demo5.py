from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://mail.163.com")
driver.maximize_window()
frame=driver.find_elements("tag name","iframe")

for i in frame:
    print(i)
print(frame[0])
print(frame[1])
print(frame[2])
driver.switch_to.frame(frame[0])
driver.find_element("name","email").send_keys("123456")
driver.switch_to.default_content()