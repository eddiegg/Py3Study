from time import ctime

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

driver= webdriver.PhantomJS()
print(ctime())
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
print('search completed '+ctime())

# print(driver.title)

