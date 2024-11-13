from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()

try:

    driver.get("https://example.com")
    time.sleep(5)

    # Wait until the <h1> element containing the specific text is present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Example Domain']"))
    )

    # Print the text of the found element
    print("Element text:", element.text)
    time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
