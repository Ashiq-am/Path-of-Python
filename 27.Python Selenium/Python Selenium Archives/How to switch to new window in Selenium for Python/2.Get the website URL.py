# Open login yahoo for sample url
driver.get("https://login.yahoo.com/")

# print title of yahoo window
print("First window title = " + driver.title)

# Clicks on privacy and it opens in new window
driver.find_element_by_class_name("privacy").click()

# switch window in 7 seconds
time.sleep(7)

# window_handles[1] is a second window
driver.switch_to.window(driver.window_handles[1])

# prints the title of the second window
print("Second window title = " + driver.title)

# window_handles[0] is a first window
driver.switch_to.window(driver.window_handles[0])

# prints windows id
print(driver.window_handles)
