while (1):

    # waiting for the webpage to load
    time.sleep(5)
    rt = driver.find_elements_by_css_selector('.css-18t94o4[data-testid ="retweet"]')
    for r in rt:
        try:
            r.click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="layers"]\
			/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()

            c -= 1
            time.sleep(2)
            if (c == 0):
                break
        except (ElementClickInterceptedException, StaleElementReferenceException):
            pass
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    if (c == 0):
        break
