from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """一些基本的页面操作"""

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except(NoSuchElementException, KeyError, ValueError) as e:
            #             self.driver.get_screenshot_as_file('../errorScreenshots/')
            print('错误信息 :%s' % (e.args[0]))

    def find_elements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except(NoSuchElementException, KeyError, ValueError) as e:
            print('错误信息 :%s' % (e.args[0]))