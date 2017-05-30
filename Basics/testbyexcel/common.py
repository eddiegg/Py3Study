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
        elif browser == 'safari':
            driver = webdriver.Safari()
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
        elif by == 'css':
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
        keywords=str(line[3])
        self.element_wait(line)
        self.get_element(line).send_keys(keywords)

    def clear(self, line):
        '''
        清除输入框文字
        '''
        self.element_wait(line)
        self.get_element(line).clear()

    def click(self, line):
        '''
        点击
        '''
        self.element_wait(line)
        el = self.get_element(line)
        el.click()

    def right_click(self, line):
        '''
        右击
        '''
        self.element_wait(line)
        el = self.get_element(line)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, line):
        '''
        鼠标悬停
        '''
        self.element_wait(line)
        el = self.get_element(line)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, line):
        '''
        双击
        '''
        self.element_wait(line)
        el = self.get_element(line)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, line):
        '''
        拖动
        '''
        self.element_wait(line[0:3])
        element = self.get_element(line[0:3])
        self.element_wait(line[3:6])
        target = self.get_element(line[3:6])
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, line):
        '''
        点击文字
        '''
        self.driver.find_element_by_partial_link_text(line[3]).click()

    def close(self):
        '''
        点击关闭按钮
        '''
        self.driver.close()

    def quit(self,line):
        '''
        关闭浏览器
        '''
        self.driver.quit()

    def submit(self, line):
        '''
        提交表单
        '''
        self.element_wait(line)
        el = self.get_element(line)
        el.submit()

    def F5(self):
        '''
        刷新页面
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        执行js

        例:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, line, attribute):
        '''
        获取元素指定属性

        '''
        el = self.get_element(line)
        return el.get_attribute(attribute)

    def get_text(self, line):
        '''
        获取元素文字属性
        '''
        self.element_wait(line)
        el = self.get_element(line)
        return el.text

    def get_display(self, line):
        '''
        检查特定元素是否显示
        '''
        self.element_wait(line)
        el = self.get_element(line)
        return el.is_displayed()

    def get_title(self,line):
        '''
        获取窗口标题
        '''
        return self.driver.title

    def get_url(self):
        '''
        获取URL
        '''
        return self.driver.current_url

    def get_windows_img(self, file_path='./img/'):
        '''
        当前窗口截图并保存到指定位置
        '''
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        '''
        隐式等待

        例:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        确定弹窗

        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        取消弹窗
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, line):
        '''
        切换到指定frame
        '''
        self.element_wait(line)
        iframe_el = self.get_element(line)
        self.driver._switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        从当前frame切换到默认frame
        '''
        self.driver._switch_to.default_content()

    def open_new_window(self, line):
        '''
        开启并转移到新窗口
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(line)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)

    def verify_attribute(self, line):
        '''
        检查元素attribute值是否符合预期
        '''
        if(self.get_attribute(line,line[0]) == line[6]):
            return "验证通过"
        else:
            return "验证失败"

