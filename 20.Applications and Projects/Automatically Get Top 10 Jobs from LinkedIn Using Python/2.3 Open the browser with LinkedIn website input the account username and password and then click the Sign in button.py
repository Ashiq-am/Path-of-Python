from clicknium import clicknium as cc, locator

# Create a browser instance with
# "cc.chrome", for edge browser using "cc.edge"
# Open browser with specified url and
# get browser tab For default, it will
# wait the page load completely. You do
# not need to add extra time.sleep()
_tab = cc.chrome.open("https://www.linkedin.com/", is_wait_complete=True)

# Find input box for username
# Fill in with the key value 'linkedin_login_name'
# in setting.json
_tab.find_element(locator.chrome.linkedin.login.login_email).set_text(
	Setting.login_name)

# Find input box for password
# Fill in with the key value 'linkedin_login_password'
# in setting.json
_tab.find_element(locator.chrome.linkedin.login.login_password).set_text(
	Setting.login_password)

# Find submit button, and click it to login
_tab.find_element(locator.chrome.linkedin.login.signin).click()

# Wait skip add phone button appears in 5 seconds,
# if it exists, click the 'skip' button
_tab.wait_appear(locator.chrome.linkedin.login.skip_add_phone,
				wait_timeout=5).click()
