from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# create instance of Chrome webdriver
driver=webdriver.Chrome(ChromeDriverManager().install())
