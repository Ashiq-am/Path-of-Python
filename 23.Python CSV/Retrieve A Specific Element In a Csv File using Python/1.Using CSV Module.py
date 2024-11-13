import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        if row[0] == 'ReactJS':
            print(f"Description of ReactJS: {row[1]}")
