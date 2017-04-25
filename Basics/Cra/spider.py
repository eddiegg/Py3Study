
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

browser = webdriver.PhantomJS(service_args=['--load-images=false'])
# browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
# browser = webdriver.Firefox()
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

def main():
    print('started')
    get_products()
    browser.quit()
    print('quit')

if __name__ == '__main__':
    main()