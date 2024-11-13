from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Creating an instance
driver = webdriver.Chrome("Enter-Location-Of-Your-Web-Driver")

# Logging into LinkedIn
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element_by_id("username")
username.send_keys("") # Enter Your Email Address

pword = driver.find_element_by_id("password")
pword.send_keys("")	 # Enter Your Password

driver.find_element_by_xpath("//button[@type='submit']").click()

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"

driver.get(profile_url)	 # this will open the link
