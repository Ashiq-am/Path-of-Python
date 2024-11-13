# embedding html doc into BeautifulSoup
soup = BeautifulSoup(ht_doc, 'html.parser')

# embedding a tag into link variable
link = soup.a
print(link)

# iterating through parent in link variable
for parent in link.parents:

    # printing statement for Parent is empty case
    if parent is None:
        print(parent)
    else:
        print(parent.name)
