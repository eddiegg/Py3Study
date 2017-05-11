
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from time import sleep

browser = webdriver.PhantomJS(service_args=['--load-images=false'])
# browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
# browser = webdriver.Chrome()
browser.set_window_size(1280,800)
wait = WebDriverWait(browser, 10)

def get_products():
    browser.get('https://miaosha.jd.com/category.html?cate_id=29')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".catinfo_seckillnow .seckill_mod_goods")))
    html = browser.page_source
    doc = pq(html)
    products=[]
    items = doc(".catinfo_seckillnow .seckill_mod_goods").items()
    for item in items:
        product={
            'name': item.find('.seckill_mod_goods_title').text(),
            'price': item.find('.seckill_mod_goods_price_now').text()[2:].replace(" ",'')
        }
        products.append(product)
    products.sort(key=lambda item: float(item['price']))
    for i in products:
        print(i)

def login():
    browser.get("http://121.196.200.171:7650/#/")
    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"form>div:nth-child(2)>div>input")))
    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"form>div:nth-child(3)>div>input")))
    sub = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"form>div.form-actions>div.col-md-8>button.btn.blue.pull-right")))
    username.send_keys("eddie")
    password.send_keys("666666qxb!")
    sub.click()

def get_menus():
    login()
    content_mgr = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                "div>ul>li:nth-child(6)>a>span.title.ng-binding")))
    content_mgr.click()
    hot_words = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                "div>ul>li.ng-scope.open>ul>li:nth-child(1)>a")))
    hot_words.click()
    print(hot_words.text)


if __name__ == '__main__':
    get_menus()