# function to get next post
def next_post():
	try:
		nex = chrome.find_element_by_class_name("coreSpriteRightPaginationArrow")
		return nex
	except selenium.common.exceptions.NoSuchElementException:
		return 0
