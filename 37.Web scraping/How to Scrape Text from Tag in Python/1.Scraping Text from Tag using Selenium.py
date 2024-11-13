from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

dr = webdriver.Chrome(options=options)
dr.get("https://www.geeksforgeeks.org/machine-learning-types-of-artificial-intelligence/")

st = dr.find_elements(By.TAG_NAME, 'strong')
for i in st:
  print(i.text)
dr.quit()
