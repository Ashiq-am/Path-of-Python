from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the desired webpage
    driver.get("https://example.com")
    time.sleep(5)

    try:

        element = driver.find_element(By.CSS_SELECTOR, 'h1')

        # Print the text of the located element
        print(f"Element text: {element.text}")


    except NoSuchElementException:
        # Handle the case where the element is not found
        print("Element with the specified CSS selector was not found.")

finally:
    # Close the browser
    driver.quit()
