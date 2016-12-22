#-*-coding:utf-8-*-
#======================利用selenium模拟登陆知乎==============================
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://www.zhihu.com/#signin'
driver.get(url)
#防止页面加载个没完
driver.set_page_load_timeout(10)
driver.find_element_by_name("account").send_keys('15821893153')
driver.find_element_by_name('password').send_keys('czp8852887')

#输入验证码
time.sleep(10)
driver.find_element_by_class_name('sign-button').click()
time.sleep(2)
#获取页面源代码
#driver.get('https://www.zhihu.com/people/xiao-shi-16-15')
#time.sleep(2)
#print driver.page_source
driver.find_element_by_xpath("html/body/div[3]/div[1]/div/div[1]/div[2]/ul/li[3]/a").click()
time.sleep(4)
driver.quit()


