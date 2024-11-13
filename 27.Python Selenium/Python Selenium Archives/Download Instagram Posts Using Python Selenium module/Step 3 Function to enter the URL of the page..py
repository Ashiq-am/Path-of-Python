# extract URL
def url_name(url):
    # the web page opens up
    chrome.get(url)

    # webdriver will wait for 4 sec before throwing a
    # NoSuchElement exception so that the element
    # is detected and not skipped.
    time.sleep(4)
