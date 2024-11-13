# Necessary webdrivers ned to be imported
from selenium import webdriver
# Get the instance of the webBrowser
# window, here we are using Chrome
webBrowser = webdriver.Chrome()

# Lets open google.com in the first tab
webBrowser.get('http://google.com')

# Lets open https://www.bing.com/ in the second tab
webBrowser.execute_script("window.open('about:blank', 'secondtab'),")
webBrowser.switch_to.window("secondtab")
webBrowser.get('https://www.bing.com/')

# Lets open https://www.facebook.com/ in the third tab
webBrowser.execute_script("window.open('about:blank', 'thirdtab'),")
webBrowser.switch_to.window("thirdtab")
webBrowser.get('https://www.facebook.com/')
