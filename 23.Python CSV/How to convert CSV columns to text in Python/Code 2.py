# reading csv file
text = open("datasets/Fruit.csv", "r")

# joining with space content of text
text = ' '.join([i for i in text])

# replacing ',' by space
text = text.replace(",", " ")

#displaying result
print(text)
