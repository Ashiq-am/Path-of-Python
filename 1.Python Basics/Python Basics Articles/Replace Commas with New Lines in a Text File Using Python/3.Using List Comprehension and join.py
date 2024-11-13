with open('file.txt', 'r') as file:
    lines = [line.replace(',', '\n') for line in file]

with open('output.txt', 'w') as file:
    file.writelines(lines)
