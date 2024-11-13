with open('example.txt', 'r+') as file:
    content = file.read()
    file.write('\nThis is a new line.')
