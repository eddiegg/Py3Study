import unittest
from selenium import webdriver
from WebDemo.pages.MainPage import MainPage

class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://www.baidu.com'

    def tearDown(self):
        self.driver.quit()

    def testSearch(self):
        mainPage = MainPage(self.driver)
        mainPage.open(self.url)
        mainPage.search('python3')
