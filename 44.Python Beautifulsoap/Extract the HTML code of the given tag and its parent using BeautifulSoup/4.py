# getting the HTML of the parent parent of
# the h1 tag we parsed earlier
parent = soup.find("span",
				attrs={"id": 'Machine_learning_approaches'}).parent()
print(parent)
