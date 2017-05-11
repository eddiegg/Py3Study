from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.PhantomJS(service_args=['--load-images=false'])
# browser = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
browser = webdriver.Chrome()
browser.set_window_size(1280,800)
wait = WebDriverWait(browser, 10)
browser.get('http://www.tianyancha.com')

listCom = open("F:\\compare\\qxb_hangzhou_0504.csv")
found = []
not_found =[]
count = 1
for item in listCom:
    print("搜索"+str(count))
    count = count + 1
    item = item.replace('\n','')
    inp = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#live-search'))
    )
    inp.send_keys(item)
    sub = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "#ng-view > div > div.mainV3_tab1 > div.mainv2_tab1 > div > div.main-tab-outer > div:nth-child(2) > div > div.input-group.inputV2.ng-scope > div > span"))
    )
    sub.click()
    sub1 = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id=\"ng-view\"]/div[2]/div/div/div[1]/div[1]/div[1]/div/span[2]"))
    )

    # try:
    #     text1 = browser.find_element_by_xpath("//*[@id=\"ng-view\"]/div[2]/div/div/div[1]/div[5]/div/div[1]").text
    #     if text1 == "没有找到相关结果":
    #         not_found.append(item)
    try:
        text = browser.find_element_by_xpath(
            '//*[@id="ng-view"]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/a/span/em').text
        if item == text:
            found.append(item)
            print("找到："+str(len(found)))
        else:
            not_found.append(item)
    except:
        not_found.append(item)


    sub2 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ng-view\"]/div[1]/div/div/div[1]/div[1]"))
    )
    sub2.click()
    sleep(1)

print(len(not_found))
print(len(found))
listCom.close()
print("done")
