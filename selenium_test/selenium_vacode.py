# coding=utf-8
from splinter import Browser
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def log_in_douban(Name='', PassWord=''):
    if Name and PassWord:
        bs = Browser('chrome')
        bs.visit(url='https://www.douban.com/accounts/login?source=main')
        if bs.is_element_present_by_id(id='email'):
            bs.find_by_id(id='email').fill(Name)
            bs.find_by_id(id='password').fill(PassWord)
            if bs.is_element_present_by_id(id='captcha_field'):
                # bs.find_by_id('captcha_field').fill(code_img)
                while True:
                    val = bs.find_by_id(id='captcha_field').first.value
                    if val and len(val) > 0:
                        bs.find_by_id('captcha_field').fill(val)
                        break
                    pass
                pass
            bs.find_by_name('login').click()
            print 'log in'


if __name__ == '__main()__':
    log_in_douban(Name='wuzhiyi51@sina.com', PassWord='649911812')
