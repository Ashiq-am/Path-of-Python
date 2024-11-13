# Empty list to store the output
urls = []

# For loop that iterates over all the <li> tags
for h in soup.findAll('li'):

    # looking for anchor tag inside the <li>tag
    a = h.find('a')
    try:

        # looking for href inside anchor tag
        if 'href' in a.attrs:
            # storing the value of href in a separate
            # variable
            url = a.get('href')

            # appending the url to the output list
            urls.append(url)

    # if the list does not has a anchor tag or an anchor
    # tag does not has a href params we pass
    except:
        pass
