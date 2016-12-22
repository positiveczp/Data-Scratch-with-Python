#-*-coding:utf-8-*-
#======================利用selenium模拟登陆淘宝==============================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time

url = 'https://i.taobao.com/my_taobao.htm?nekot=Y3pwMTg4MjUxNTk3MjY%3D1472184661233'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
#执行JS代码，显示出登录框
driver.execute_script("document.getElementById('J_StaticForm').removeAttribute('class')")
time.sleep(2)

#模拟登陆
driver.find_element_by_name("TPL_username").send_keys('czp18825159726')
driver.find_element_by_name("TPL_password").send_keys('czpczp*****')
driver.find_element_by_xpath(".//*[@id='J_SubmitStatic']").click()
time.sleep(2)
#获取页面源代码
driver.get("https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.a2109.d1000368.RqA3ix")
time.sleep(2)
print driver.page_source
driver.close()















































