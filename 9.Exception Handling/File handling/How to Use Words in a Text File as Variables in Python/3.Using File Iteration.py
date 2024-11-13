# Open the file
with open("words.txt", "r") as file:
    for line in file:
        word = line.strip()
        print(f"{word} = Fruit")
