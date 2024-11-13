# I have used f-strings to format the string
c = 1
for x in range(3, 9):
	print(f"Heading {c}: ")
	c += 1
	curr_path = f'/html/body/c-wiz/div/div[2]/div[2]/div/main\
	/c-wiz/div[1]/div[{x}]/div/div/article/h3/a'
	title = driver.find_element_by_xpath(curr_path)
	print(title.text)
