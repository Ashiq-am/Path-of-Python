# Necessary imports
from selenium import webdriver

# initially webdriver is empty
webdriver.driver = None
browserName = input("Enter your browser name(chrome/firefox/edge/ie):")

# Depends upon the browser name, drivers are selected,
# in order to check for all given 4 browser checkings,
# all 4 drivers must be installed and they should be
# available in "Path"
if browserName.upper() == "CHROME":
    driver = webdriver.Chrome()
elif browserName.upper() == "FIREFOX":
    driver = webdriver.Firefox()
elif browserName.upper() == "EDGE":

    # MicrosoftWebDriver.exe should be
    # downloaded and available in Path
    driver = webdriver.Edge()
elif browserName.upper() == "IE":

    # IEDriverServer.exe should be
    # downloaded and available in Path
    driver = webdriver.Ie()
else:
    print("No browser is specified")

# Lets open google.com in the first tab
driver.get('http://google.com')

# Lets open https://www.bing.com/ in the second tab
driver.execute_script("window.open('about:blank','secondtab'),")
driver.switch_to.window("secondtab")
driver.get('https://www.bing.com/')

# Lets open https://www.facebook.com/ in the third tab
driver.execute_script("window.open('about:blank','thirdtab'),")
driver.switch_to.window("thirdtab")
driver.get('https://www.facebook.com/')

# It is always good to quit the driver
# driver.quit()
