def scrape_info(self, html):
    soup = BeautifulSoup(html, "html5lib")
    web_page_paragraph_contents = soup('p')
    text = ''

    for para in web_page_paragraph_contents:
        if not ('https:' in str(para.text)):
            text = text + str(para.text).strip()
    print('\n <-----Text Present in The WebPage is--->\n', text, '\n')
    return
