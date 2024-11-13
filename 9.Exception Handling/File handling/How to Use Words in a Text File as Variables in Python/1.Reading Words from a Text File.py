# Open the file
with open("fruits.txt", "r") as file:
    # Read all lines from the file
    lines = file.readlines()

# Initialize an empty list to store the words
words = []

# Loop through each line in the file
for line in lines:
    word = line.strip()
    words.append(word)

# Now you can use the words as variables
for word in words:
    print(f"{word} = Fruit")
