from WebDemo.public.BasePage import BasePage
from WebDemo.pageElements.PageElements import MainPageEls

class MainPage(BasePage):

    def search(self, word):
        self.driver.find_element(*MainPageEls.inputbox).clear()
        self.driver.find_element(*MainPageEls.inputbox).send_keys(word)
        self.driver.find_element(*MainPageEls.search).click()
