from selenium import webdriver


#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()


def infinteScroll(driver):
    height = 0
    i = 0
    while height < driver.execute_script("return document.body.scrollHeight"):
        print(i)
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        i = i+1
    html_source = driver.page_source.encode('utf-8')
    return html_source
