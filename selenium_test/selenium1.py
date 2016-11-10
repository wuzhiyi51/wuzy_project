# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def s(int):
    time.sleep(int)


browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
print '浏览器最大化'
browser.maximize_window()
text = browser.find_element_by_name('tj_duty').text
print text  # 打印文案

browser.find_element_by_id('kw').send_keys('selenium')
print browser.find_element_by_id('kw').get_attribute('type')
print browser.find_element_by_id('kw').size  # 打印输入框的大小
browser.find_element_by_id('su').click()
time.sleep(3)

print '设置浏览器宽480，高800显示'
browser.set_window_size(480, 800)
browser.get('http://m.mail.10086.cn')
time.sleep(3)

print '回到刚才的页面'
browser.back()
time.sleep(3)

print '百度搜索selenium'
browser.get('http://www.baidu.com')
browser.maximize_window()
browser.find_element_by_xpath('//*[@id="kw"]').send_keys(u'json')
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)

browser.quit()

browser = webdriver.Chrome()
print '人人网综合应用'
browser.get('http://www.renren.com')
browser.find_element_by_id('email').clear()
browser.find_element_by_id('email').send_keys('wuzhiyi51@sina.com')
browser.find_element_by_id('email').send_keys(Keys.BACK_SPACE)
time.sleep(2)
browser.find_element_by_id('email').clear()
browser.find_element_by_id('email').send_keys('wuzhiyi51@sina.com')
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'a')
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'x')
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')
s(2)
browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys('649911812')
browser.find_element_by_xpath('//*[@id="login"]').send_keys(Keys.ENTER)
browser.maximize_window()
article = browser.find_element_by_link_text(u'弦来一缕国风')
ActionChains(browser).move_to_element(article).perform()
ActionChains(browser).context_click(article).perform()
time.sleep(5)

browser.quit()
