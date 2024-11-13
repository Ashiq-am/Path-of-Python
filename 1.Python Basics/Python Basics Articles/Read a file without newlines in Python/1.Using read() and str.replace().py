with open('file.txt', 'r') as file:
    content = file.read().replace('\n', ' ')
print(content)
