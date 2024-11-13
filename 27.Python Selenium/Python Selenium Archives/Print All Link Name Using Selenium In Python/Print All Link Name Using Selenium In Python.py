#import module
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# url
driver.get('https://www.youtube.com/')

# find web links
link = driver.find_elements(By.TAG_NAME, 'a')

# print name of all links
for i in link:
	print(i.text)
