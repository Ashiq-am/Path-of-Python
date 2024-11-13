# Necessary webdrivers ned to be imported
from selenium import webdriver

# This is for Firefox. Similarly if
# chrome is needed , then it has to be specified
webBrowser = webdriver.Firefox()

# This will open geeksforgeeks site in Firefox
webBrowser.get('https://www.geeksforgeeks.org/')
