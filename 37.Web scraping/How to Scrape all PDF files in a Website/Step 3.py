# created an empty list for putting the pdfs
list_of_pdf = set()

# accessed the fist p tag in the html
l = soup.find('p')

# accessed all the anchors tag from given p tag
p = l.find_all('a')

# iterate through p for getting all the href links
for link in p:
    # original html links
    print("links: ", link.get('href'))
    print("\n")

    # converting the extention from .html to .pdf
    pdf_link = (link.get('href')[:-5]) + ".pdf"

    # converted to .pdf
    print("converted pdf links: ", pdf_link)
    print("\n")

    # added all the pdf links to set
    list_of_pdf.add(pdf_link)
