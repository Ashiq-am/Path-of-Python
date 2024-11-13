from selenium import webdriver

# Create a FirefoxOptions object
options = webdriver.FirefoxOptions()

# Set the Firefox browser to run in headless mode
options.headless = True

# Create a WebDriver instance with the specified options
driver = webdriver.Firefox(options=options)

# Perform web automation tasks here
# Navigate to a website
driver.get("https://example.com")

# For example, let's print the title of the webpage
print("Page Title:", driver.title)

# Close the WebDriver when done
driver.quit()
