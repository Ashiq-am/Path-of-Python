import csv

file = 'input.txt'

# open the file in read mode
with open(file, 'r') as file:
    # create a csv reader
    reader = csv.reader(file, delimiter=':')
    # convert csv data to dictionary
    res = {row[0].strip(): row[1].strip() for row in reader}

# print the dictionary
print("Dictionary Created")
print(res)
