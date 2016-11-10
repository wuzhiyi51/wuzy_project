# coding:utf-8
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. all main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')


class SearchResultPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass


class BaiduPageLoacator(object):
    CONTENT = (By.ID, 'kw')
    GO_BUTTON = (By.ID, 'su')
