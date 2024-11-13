# importing webdriver from selenium module
from selenium import webdriver

# path for chromedriver
path_to_chromedriver ='/Users/Admin/Desktop/chromedriver'

browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.geeksforgeeks.org'
browser.get(url)
