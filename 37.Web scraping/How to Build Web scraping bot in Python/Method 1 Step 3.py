# Xpath you just copied
news_path = '/html/body/c-wiz/div/div[2]/div[2]/\
div/main/c-wiz/div[1]/div[3]/div/div/article/h3/a'

# to get that element
link = driver.find_element_by_xpath(news_path)

# to read the text from that element
print(link.text)
