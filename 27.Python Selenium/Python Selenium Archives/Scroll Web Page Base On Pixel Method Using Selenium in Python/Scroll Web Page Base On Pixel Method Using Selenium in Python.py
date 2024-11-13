from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# create instance of Chrome webdriver
driver=webdriver.Chrome(ChromeDriverManager().install())

#url
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#maximize window
driver.maximize_window()

#scroll by pixcel
driver.execute_script("window.scrollBy(0,2000)","")
time.sleep(4)
