#-*-coding:utf-8-*-
#======================利用selenium模拟登陆 电脑版 微博==============================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import selenium.common.exceptions
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = 'http://weibo.com/'
driver.get(url)

#时间设置很重要，否则可能会出现异常
try:
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"username")))
    driver.find_element_by_xpath(".//*[@id='loginname']").send_keys('18825159726')
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div/div[3]/div[2]/div/input").send_keys('czp******')
    #driver.find_element_by_name("username").send_keys('18825159726')
    #driver.find_element_by_name("password").send_keys('czp******')
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div/div[3]/div[6]/a").click()
    time.sleep(2)
    print driver.page_source

except selenium.common.exceptions.TimeoutException:
    print 'TimeoutException!'

finally:
    #当只打开一个窗口时，driver.close() = driver.quit()
    driver.close()







