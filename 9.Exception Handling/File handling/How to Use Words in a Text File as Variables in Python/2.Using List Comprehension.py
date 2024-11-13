# Read words from the file using list comprehension
with open("words.txt", "r") as file:
    words = [line.strip() for line in file]

# Now you can use the words as variables
for word in words:
    print(f"{word} = Fruit")
