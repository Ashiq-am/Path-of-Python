import undetected_chromedriver as uc
import pickle

driver = uc.Chrome()
driver.get('https://geeksforgeeks.org')

# Load cookies from a file
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

# We can continue with our automation
# ...

# Close the browser
driver.quit()
