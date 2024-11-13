# Since there are only one table in
# our doc file we are using 0. For multiple tables
# you can use suitable for toop
table = doc.tables[0]

# Initializing some empty list
list1 = []
list2 = []

# Looping through each row of table
for i in range(len(table.rows)):

    # Looping through each column of a row
    for j in range(len(table.columns)):
        # Extracting the required text
        list1.append(table.rows[i].cells[j].paragraphs[0].text)

    list2.append(list1[:])
    list1.clear()

print(list2)
