# coding=utf-8
from splinter import Browser
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def log_in_doban(Name='', PassWrod=''):
    if Name and PassWrod:
        bs = Browser('chrome')
        bs.visit(url='http://www.douban.com/accounts/login?source=main')
        if bs.is_element_present_by_id(id='email'):
            bs.find_by_id(id='email').fill(Name)
            bs.find_by_id(id='password').fill(PassWrod)
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
            # bs.quit()


if __name__ == '__main__':
    log_in_doban(Name='wuzhiyi51@sina.com', PassWrod='649911812')
