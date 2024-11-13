# Python program to login to the Geeksforgeeks
# using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

chromedriver_path = '<chrome web driver path>'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

try:
    # Opening the geeksforgeeks website
    webdriver.get('https://www.geeksforgeeks.org/')

    # Clicking on the sign in button
    signIn = webdriver.find_element_by_css_selector('#userProfileId > a')
    signIn.click()
    sleep(4)

    # Finding the username input field and sending the username
    username = webdriver.find_element_by_css_selector('#luser')
    username.send_keys('<Geeksforgeeks Username>')

    # Finding the password inpute field and sending password
    password = webdriver.find_element_by_css_selector('#password')
    password.send_keys('<Geeksforgeeks password>')

    # Pressing enter on the signin button
    button_login = webdriver.find_element_by_css_selector(
        '#Login > button')
    button_login.click()
    sleep(6)

finally:
    webdriver.close()
