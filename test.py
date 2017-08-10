from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


## System.setProperty("webdriver.gecko.driver", "/Users/hectester/Documents");
## 创建浏览器对象
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.set_window_size(1680, 1080)
## 打开SYG页面
browser.get('http://10.10.10.54:2334/product/SKII-0066')
time.sleep(4)
login_elem = browser.find_element_by_xpath('/html/body/div/header/div/div[2]/a[1]/span')

login_elem.click()

account_elem = browser.find_element_by_id('account')
password_elem = browser.find_element_by_id('password')

account_elem.send_keys('13800001111')
password_elem.send_keys('a123456')
account_elem.click()

time.sleep(0.5)

login_btn = browser.find_element_by_id('submit_btn')
login_btn.click()

time.sleep(10)
browser.quit()
