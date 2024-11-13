# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create instance of Chrome webdriver
driver = webdriver.Chrome()
driver.get("https://account.booking.com/sign-in?op_token=EgVvYXV0aCLdAgoUdk8xS2Jsazd4WDl0VW4yY3BaTFMSCWF1dGhvcml6ZRo1aHR0cHM6Ly9zZWN1cmUuYm9va2luZy5jb20vbG9naW4uaHRtbD9vcD1vYXV0aF9yZXR1cm4q_AFVcm9CSnFTUk5fY0p6TzJ2d0VuTzdycl92NzBncExyTEZ1TDc0Z2RlNlB2Tnc5T1FscEFISEI5MlpWVGZpNFd1eWplaDE0dm50S0Q5aHBXM3ladWdpLXY0SEZoLVFhRDdSbGk5dkRzSmN0MmE4ZXNpZEU1VHo0WkRyTDB3M3Y5Um9UNEU3dUh1SzMxZXNfTmM3Q2l4NWtNUkxpRFk0cnhEVVBaRXo5enJXV2psdVBnNHBpUlBNaUh4LUJzRTNSWVA1Z19WVWRSSHdOQTVzcWhGVGkzSDlET013dUJFWHY4dThsQjE4Z3BfdUJJLUtGaDQxSUgzcGYxWGx1TkVCBGNvZGUqFgiOyBIwwaf46Ii8JDoAQgBYgd3j_AU")

# find the element where we have to
# enter the xpath
# fill the email
driver.find_element_by_xpath('//*[@id="username"]').send_keys('xxxxxx.com')

# click on next button
driver.find_element_by_xpath(
	'//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span').click()

# find the element where we have to
# enter the xpath
# fill the password
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Praxxxxx')

# find the element Sign in
# request using xpath
# clicking on that element
driver.find_element_by_xpath(
	'//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div/form/button/span').click()
