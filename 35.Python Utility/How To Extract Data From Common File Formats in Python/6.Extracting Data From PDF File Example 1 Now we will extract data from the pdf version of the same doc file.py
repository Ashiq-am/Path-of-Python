# import module
import fitz

# Reading our pdf file
docu = fitz.open('file.pdf')

# Initializing an empty list where we will put all text
text_list = []

# Looping through all pages of the pdf file
for i in range(docu.pageCount):
    # Loading each page

    pg = docu.loadPage(i)

    # Extracting text from each page
    pg_txt = pg.getText('text')

    # Appending text to the empty list
    text_list.append(pg_txt)

# Cleaning the text by removing useless
# empty strings and unicode character '\u200b'
text_list = [i.replace(u'\u200b', '') for i in text_list[0].split('\n') if len(i.strip()) != 0]
print(text_list)
