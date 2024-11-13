import undetected_chromedriver as uc
import json

driver = uc.Chrome()
driver.get('https://geeksforgeeks.org')

# Load cookies from a JSON file
with open('cookies.json', 'r') as file:
    cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

# We can continue with our automation
# ...

# Close the browser
driver.quit()
