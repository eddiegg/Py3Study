from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Common(object):
    '''
    封装常用的动作接口
    '''

    def __init__(self, browser='ff'):
        '''
        选择测试用的浏览器
        '''
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, line):
        '''
        等待元素出现
        Usage:
        
        '''
        wait = WebDriverWait(self.driver, 10)

        by = line[1]
        value = line[2]

        if by == "id":
            wait.until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            wait.until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            wait.until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("请检查excel中得定位方法:'id','name','class','link_text','xpath','css'.")

    def get_element(self,line):
        '''
        获取目标元素
        '''
        by = line[1]
        value = line[2]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("请检查excel中得定位方法,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        '''
        打开指定网址.

        例:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        最大化窗口
        
        例:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        根据指定宽、高设定浏览器窗口大小
        
        例:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def type(self, line):
        '''
        输入框中输入指定文字

        '''
        self.element_wait(line[1:3])
        el = self.get_element(line[1:3])
        el.send_keys(line[3])

    def clear(self, line):
        '''
        清除输入框文字

        '''
        self.element_wait(line[1:3])
        el = self.get_element(line[1:3])
        el.clear()

    def click(self, line):
        '''
        点击
        '''
        self.element_wait(line[1:3])
        el = self.get_element(line[1:3])
        el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)
