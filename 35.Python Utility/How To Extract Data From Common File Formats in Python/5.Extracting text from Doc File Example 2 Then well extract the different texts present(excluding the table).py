# Getting all the text in the doc file
l=[doc.paragraphs[i].text for i in range(len(doc.paragraphs))]

# There might be many useless empty
# strings present so removing them
l=[i for i in l if len(i)!=0]
print(l)
