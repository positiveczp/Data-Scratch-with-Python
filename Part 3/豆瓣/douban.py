#-*-coding:utf-8-*-
#======================利用selenium模拟登陆豆瓣==============================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

url = "https://www.douban.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#模拟登陆
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"form_email")))
driver.find_element_by_name("form_email").send_keys('15821893153')
driver.find_element_by_name("form_password").send_keys('czp******')
driver.find_element_by_xpath(".//*[@id='lzform']/fieldset/div[3]/input").click()
time.sleep(2)

#获取页面源代码
driver.get("https://www.douban.com/")
time.sleep(2)
print driver.page_source
driver.close()





























































