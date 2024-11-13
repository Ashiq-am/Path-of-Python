def login(username, your_password):
    log_but = chrome.find_element_by_class_name("L3NKy")
    time.sleep(2)
    log_but.click()
    time.sleep(4)

    # finds the username box
    usern = chrome.find_element_by_name("username")

    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = chrome.find_element_by_name("password")

    # sends the entered password
    passw.send_keys(your_password)

    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)

    # Finding Not Now button
    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(3)
