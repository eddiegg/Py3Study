from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """一些基本的页面操作"""

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)


    def find_element(self, *loc):
        try:
            # WebDriverWait(self.driver, 0).until(lambda driver: driver.find_element(*loc).is_displayed())
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(*loc))
            return self.driver.find_element(*loc)
        # except(NoSuchElementException, KeyError, ValueError) as e:
        #     #             self.driver.get_screenshot_as_file('../errorScreenshots/')
        #     print('错误信息 :%s' % (e.args[0]))
        except TimeoutException:
            return self.find_element(self, *loc)

    def find_elements(self, *loc):
        try:
            return self.driver.find_elements(*loc)
        except(NoSuchElementException, KeyError, ValueError) as e:
            print('错误信息 :%s' % (e.args[0]))