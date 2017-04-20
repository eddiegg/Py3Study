from selenium import webdriver
import logging
import xml.dom.minidom
logging.basicConfig(level=logging.INFO)
driver = webdriver.Firefox()
driver.get("http://www.qixin.com")
driver.maximize_window()
# print(driver.title)

