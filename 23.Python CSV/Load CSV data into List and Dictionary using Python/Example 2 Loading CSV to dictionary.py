import csv

filename = "Geeks.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        print(line)
