#-*-coding:utf-8-*-
#======================利用selenium模拟登陆qq空间==============================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
import time

driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
driver.maximize_window()
driver.get('http://qzone.qq.com/')
#登陆表单在页面的框架中，需要切换到该框架
#定位到iframe,参数可以是name/id
driver.switch_to_frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()

#模拟登陆
elem_user = driver.find_element_by_name("u")
elem_user.send_keys('1961674039')
elem_pwd = driver.find_element_by_name('p')
elem_pwd.send_keys('czp*****')
driver.find_element_by_class_name('btn').click()

time.sleep(2)
driver.get("http://user.qzone.qq.com/1961674039")
time.sleep(2)
print driver.page_source
driver.close()
















































