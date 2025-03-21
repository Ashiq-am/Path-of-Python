# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open Chrome
driver = webdriver.Chrome(
	'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')

# Open URL
driver.get('https://forms.gle/vWVmojtWdfFvEj8V6')

# wait for one second, until page gets fully loaded
time.sleep(1)

# Data
datas = [
	['Mary D Joiner', 'MaryDJoiner@gmail.com', '4079025063',
		'2474 McDonald Avenue,Maitland', 'NA'],
	['Karen B Johnson', 'KarenBJohnson@gmail.com',
		'3153437575', '2143 Oak Street,GRAND ISLE', 'NA'],
]

# Iterate through each data
for data in datas:
	# Initialize count is zero
	count = 0

	# contain input boxes
	textboxes = driver.find_elements_by_class_name(
		"quantumWizTextinputPaperinputInput")

	# contain textareas
	textareaboxes = driver.find_elements_by_class_name(
		"quantumWizTextinputPapertextareaInput")

	# Iterate through all input boxes
	for value in textboxes:
		# enter value
		value.send_keys(data[count])
		# increment count value
		count += 1

	# Iterate through all textareas
	for value in textareaboxes:
		# enter vlaue
		value.send_keys(data[count])
		# increment count value
		count += 1

	# click on submit button
	submit = driver.find_element_by_xpath(
		'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
	submit.click()

	# fill another response
	another_response = driver.find_element_by_xpath(
		'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
	another_response.click()

# close the window
driver.close()
