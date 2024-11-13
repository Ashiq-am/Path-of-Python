import undetected_chromedriver as uc
import pickle

driver = uc.Chrome()
driver.get('https://geeksforgeeks.org')

# Perform actions (e.g., log in)
# ...

cookies = driver.get_cookies()
print(cookies)
with open('cookies.pkl', 'wb') as file:
    pickle.dump(cookies, file)

print("Cookies saved successfully.")

# Close the browser
driver.quit()
