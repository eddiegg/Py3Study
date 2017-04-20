from selenium import webdriver
import logging
import xml.dom.minidom
logging.basicConfig(level=logging.INFO)
driver = webdriver.Firefox()
driver.get("http://www.qixin.com")
driver.add_cookie({'name':'sid','value':'s%3AUphC7ZJz9EvH74D6RlMl39AEeBHfK00c.0i7ZF6yjLcuI6xOlU%2BiRWVR%2BA%2BR89RDbIbyBct%2BFJrs','domain':'www.qixin.com'})
driver.maximize_window()
# print(driver.title)

