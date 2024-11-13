# function to check if the post is nested
def nested_check():
    try:
        time.sleep(1)
        nes_nex = chrome.find_element_by_class_name('coreSpriteRightChevron ')
        return nes_nex

    except selenium.common.exceptions.NoSuchElementException:
        return 0
