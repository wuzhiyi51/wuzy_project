# coding:utf-8
from selenium import webdriver
import unittest
import time
import page


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        time.sleep(3)

    def test_badidu_search(self):
        pass

    def tearDown(self):
        self.driver.close()
