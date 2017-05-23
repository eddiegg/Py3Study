from time import ctime
from testbyexcel import common
from selenium import webdriver

# driver = webdriver.Firefox()
# driver = webdriver.Remote(
#     command_executor= 'http://0.0.0.0:4444/wd/hub',
#     desired_capabilities={
#         'platform':'ANY',
#         'browserName':'htmlunit',
#         'version':''
#     }
# )
from selenium.webdriver import DesiredCapabilities

driver= common()
print(ctime())
driver.get("http://www.qixin.com")
driver.set_window_size(1920,1080)
cookie={'name':'sid','value':'s%3AHT9QqsgJt7peDpuKm5v1xHIWMH86y-hc.Pkp5AmvF6mFp3zsNoPDECrYT1vyLWeJqTlg73dm8oX4'}
driver.add_cookie(cookie)
searchel = driver.find_element_by_class_name("top-section")
driver.find_element_by_xpath('//*[@id="inputPlaceholderKey"]').send_keys('华为')
driver.find_element_by_class_name("btn btn-index-search").click()

# print(driver.title)

