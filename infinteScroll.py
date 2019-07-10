from selenium import webdriver

def infinteScroll(driver):
    height = 0
    while height < driver.execute_script("return document.body.scrollHeight"):
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    html_source = driver.page_source.encode('utf-8')
    return html_source

def main():
    inputLink = input("")
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.get(inputLink)
    infinteScroll(driver)
    
    
if __name__ == "__main__":
    main()
