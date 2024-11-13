file_path = 'example.txt'

with open(file_path, 'r') as file:
    file_content = ''
    line = file.readline()

    while line:
        file_content += line
        line = file.readline()

print(file_content)
