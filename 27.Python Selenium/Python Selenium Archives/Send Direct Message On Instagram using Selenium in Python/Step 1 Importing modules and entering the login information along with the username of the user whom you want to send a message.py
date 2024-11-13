from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random

# Login Credentials
username = input('Enter your Username ')
password = input('Enter your Password ')
url = 'https://instagram.com/' + input('Enter username of user whome you want to send message')
