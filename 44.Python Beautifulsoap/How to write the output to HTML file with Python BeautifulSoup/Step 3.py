# open the file in w mode
# set encoding to UTF-8
with open("output.html", "w", encoding='utf-8') as file:
    # prettify the soup object and convert it into a string
    file.write(str(soup.prettify()))
