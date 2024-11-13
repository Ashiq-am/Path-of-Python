# first pop-up box
self.bot.find_element_by_xpath(
	'//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)

# 2nd pop-up box
self.bot.find_element_by_xpath(
	'/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(4)
