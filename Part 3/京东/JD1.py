#-*-coding:utf-8-*-
#======================利用selenium模拟登陆京东==============================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

url = "https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fhome.jd.com%2Findex.html"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#模拟登陆
driver.find_element_by_class_name("checked").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loginname")))
driver.find_element_by_name("loginname").send_keys('15821893153')
driver.find_element_by_name("nloginpwd").send_keys('czp*****')
driver.find_element_by_xpath(".//*[@id='loginsubmit']").click()
time.sleep(2)

#获取页面源代码
driver.get("http://order.jd.com/center/list.action")
time.sleep(2)
print driver.page_source
print driver.title
driver.close()





























































