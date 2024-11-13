# Importing necessary modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

# Target URL
driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")

# print(driver.title)

# Printing the whole body text
print(driver.find_element_by_xpath("/html/body").text)

# Closing the driver
driver.close()
