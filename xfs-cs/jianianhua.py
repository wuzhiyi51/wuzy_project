# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class JiaNianHua(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://dev-cs.xinfushe.cn/activity/jianianhua')
        self.browser.maximize_window()

    def test_activity1_order(self):
        self.browser.find_element_by_xpath('//*[@id="appoint-btn"]').click()
        time.sleep(3)
        assert u'公司名称' in self.browser.page_source
        print '活动一我要预约跳转成功'

    def test_activity1_participation(self):
        self.browser.find_element_by_xpath('//*[@id="join-btn"]').click()
        time.sleep(3)
        assert u'公司名称' in self.browser.page_source
        print '活动一立即参与跳转成功'

    def test_active2_reg(self):
        self.browser.find_element_by_xpath('/html/body/div[3]/div[5]/a').click()
        time.sleep(3)
        assert u'手机号' in self.browser.page_source
        print '活动二立即注册跳转成功'

    def test_activit3_reg(self):
        self.browser.find_element_by_xpath('/html/body/div[4]/div[5]/a').click()
        time.sleep(3)
        print self.browser.current_window_handle
        time.sleep(2)
        all_handles = self.browser.window_handles
        print all_handles
        self.browser.switch_to.window(all_handles[1])
        time.sleep(2)
        assert u'生态共享•人工智能' in self.browser.page_source
        print '活动三立刻报名成功'

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
