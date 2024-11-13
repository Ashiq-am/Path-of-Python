content = ''
with open('file.txt', 'r') as file:
    for line in file:
        content += line.rstrip('\n')
print(content)
