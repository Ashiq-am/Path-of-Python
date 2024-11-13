#import module
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# url
driver.get('https://www.geeksforgeeks.org/')

# find web links
link = driver.find_elements(By.TAG_NAME, 'a')

# using len function count how many links
print(len(link))
