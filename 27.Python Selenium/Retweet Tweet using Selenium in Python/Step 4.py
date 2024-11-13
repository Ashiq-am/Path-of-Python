username = input('Enter Your Username: ')
password = getpass.getpass(prompt = 'Enter Your Password: ')

# locating the input box for username
u = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]\
/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
u.send_keys(''+str(username)+'')

# locating the input box for password
p = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/\
main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
p.send_keys(''+str(password)+'')
