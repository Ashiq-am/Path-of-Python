from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Set up the WebDriver (you may need to specify the path to your WebDriver executable)
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get("https://example.com")

    # Get and print the current window handle
    current_window_handle = driver.current_window_handle
    print(f"Current window handle: {current_window_handle}")

    # Get and print the page title
    page_title = driver.title
    print(f"Page title: {page_title}")

    # Check if the text we expect is on the page
    try:
        # Wait for an element with the expected text to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        print(f"Element text: {element.text}")
    except TimeoutException:
        print("An error occurred: The element was not found on the page within the time limit.")

finally:
    # Close the browser window
    driver.quit()
