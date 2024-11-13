# Using Selenium Chrome Webdriver to create
# a headless browser

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path="C:/chromedriver.exe",
						chrome_options=options)
driver.get(url)
