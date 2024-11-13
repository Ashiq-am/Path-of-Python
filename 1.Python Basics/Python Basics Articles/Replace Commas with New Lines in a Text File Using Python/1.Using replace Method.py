with open('file.txt', 'r') as file:
    content = file.read()

content = content.replace(',', '\n')

with open('output.txt', 'w') as file:
    file.write(content)
