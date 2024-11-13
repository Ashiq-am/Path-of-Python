import undetected_chromedriver as uc
import json

driver = uc.Chrome()
driver.get('https://geeksforgeeks.org')

# Perform actions (e.g., log in)
# ...

# Save cookies to a JSON file
cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)

# Close the browser
driver.quit()
