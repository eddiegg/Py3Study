import unittest
from selenium import webdriver
from WebDemo.pages.MainPage import MainPage

class testMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://www.baidu.com'
        print("started")

    def tearDown(self):
        print("quit")
        self.driver.quit()

    def test_Search(self):
        '''search baidu for python3'''
        mainPage = MainPage(self.driver)
        mainPage.open(self.url)
        mainPage.search('python3')
