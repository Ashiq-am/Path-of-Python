# import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from bs4 import BeautifulSoup as bs
import requests
import os

# get instagram account credentials
username = input('Enter Your User Name ')
password = input('Enter Your Password ')

# assign URL
url = 'https://instagram.com/' + \
	input('Enter User Name Of User For Downloading Posts ')
