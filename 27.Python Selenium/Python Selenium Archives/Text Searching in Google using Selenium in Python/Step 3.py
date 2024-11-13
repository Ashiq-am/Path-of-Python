if MyText == "search":
    # Automates 'copy' internally 
    pyautogui.hotkey('ctrl', 'c')

    chrome_options = webdriver.ChromeOptions()

    capabilities = {'browserName': 'chrome',
                    'javascriptEnabled': True}

    capabilities.update(chrome_options.to_capabilities())

    chromedriver_autoinstaller.install()

    # Invoking the chrome 
    driver = webdriver.Chrome()

    # Adjusting the size of the window 
    driver.set_window_size(1920, 1080)

    driver.implicitly_wait(10)

    driver.get("https://www.google.com/")

    # Place where our selected word gets pasted 
    driver.find_element_by_xpath("/html/body//form[@role='search']/div[2]/div[1]//div[@class='a4bIc']/input[@role='combobox']").send_keys(pyautogui.hotkey('ctrl', 'v'))
    
    

