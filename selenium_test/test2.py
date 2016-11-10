# coding=utf-8
from selenium import webdriver

driver = webdriver.Ie()

first_url = 'http://www.baidu.com'
print 'now access %s' % (first_url)
driver.get(first_url)
driver.maximize_window()

second_url = 'http://news.baidu.com'
print 'now access %s' % (second_url)
driver.get(second_url)

print 'back to %s ' % (first_url)
driver.back()

print 'foward to %s ' % (second_url)
driver.forward()

driver.quit()
