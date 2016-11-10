# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Ie()
driver.get('http://m.mail.10086.cn')

print '设置浏览器宽480，高800显示'
driver.set_window_size(480, 800)
sleep(3)
driver.quit()
