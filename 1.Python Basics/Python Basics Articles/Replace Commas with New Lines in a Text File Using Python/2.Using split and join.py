with open('file.txt', 'r') as file:
    content = file.read()

content = '\n'.join(content.split(','))

with open('output.txt', 'w') as file:
    file.write(content)
