srch = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]\
/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div\
/form/div[1]/div/label/div[2]/div/input')

s = input('Enter the Hashtag you want to retweet: ')
srch.send_keys('#'+str(s)+'')
srch.send_keys(Keys.ENTER)
