driver.find_element_by_xpath\
    ("/html/body/div/main/div[2]/div[1]/form/div[1]/input").send_keys(linkedin_username)
driver.find_element_by_xpath\
    ("/html/body/div/main/div[2]/div[1]/form/div[2]/input").send_keys(linkedin_password)

sleep() # Number of seconds

driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
