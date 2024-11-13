# Function to save content of the current post
def save_content(class_name, img_name):
    time.sleep(0.5)

    try:
        pic = chrome.find_element_by_class_name(class_name)

    except selenium.common.exceptions.NoSuchElementException:
        print("Either This user has no images or you haven't followed this user or something went wrong")
        return

    html = pic.get_attribute('innerHTML')
    soup = bs(html, 'html.parser')
    link = soup.find('video')

    if link:
        link = link['src']
    else:
        link = soup.find('img')['src']
    response = requests.get(link)

    with open(img_name, 'wb') as f:
        f.write(response.content)

    time.sleep(0.9)
