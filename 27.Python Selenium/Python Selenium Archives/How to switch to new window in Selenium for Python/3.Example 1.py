# Open the new window
driver.execute_script("window.open()")

# window switch to new 3rd window
driver.switch_to.window(driver.window_handles[2])

# get the new url in window 3
driver.get("https://www.geeksforgeeks.org/")

# print the 3rd window title
print(driver.title)
