from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
url="https://www.google.com" #Replace it with the url of your website
driver.get(url)

try:
	button=driver.find_element(By.NAME,"btnK")
	print("element exits")
except NoSuchElementException:
	print("element not found")
