c = int(input('Max no. of Retweets: '))
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]\
/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
time.sleep(10)
