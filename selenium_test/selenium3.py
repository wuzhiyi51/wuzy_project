# coding=utf-8
from selenium import webdriver
import time


def log_in_sps(mobile='', password=''):
    if mobile and password:
        browser = webdriver.Chrome()
        url = 'https://dev-sps.xinfushe.cn/serviceLogin/serviceProviderLogin'
        browser.get(url)
        time.sleep(3)
        if browser.find_element_by_id('mobile').is_displayed():
            browser.find_element_by_id('mobile').send_keys(mobile)
            browser.find_element_by_id('password').send_keys(password)
            time.sleep(3)
            if browser.find_element_by_id('valico').is_displayed():
                print browser.find_element_by_id('valico').is_displayed()
                while True:
                    # val = browser.find_element_by_id('valico').text
                    val = raw_input('Input valico:')
                    if val and len(val) > 0:
                        print val
                        browser.find_element_by_id('valico').send_keys(val)
                        break
                    pass
                pass
            browser.find_element_by_id('loginsub').click()
            print 'log in'
            time.sleep(3)
            browser.quit()


if __name__ == '__main__':
    log_in_sps(mobile='13146751613', password='a111111')
