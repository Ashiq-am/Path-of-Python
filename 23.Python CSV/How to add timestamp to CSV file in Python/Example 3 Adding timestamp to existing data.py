# Importing required modules
import csv
from datetime import datetime

# creating a list to store the
# existing data of CSV file
rows = []

# Opening the CSV file in read mode using
# the open() module
with open(r'FILE1.csv', 'r', newline='') as file:
    # Opening another CSV file to in write mode
    # to add the data
    with open(r'FILE2.csv', 'w', newline='') as file2:

        # creating the csv reader
        reader = csv.reader(file, delimiter=',')

        # storing the data of the csv file in a list
        for row in reader:
            rows.append(row)

        # creating the csv writer
        file_write = csv.writer(file2)

        # Iterating over all the data in the rows
        # variable
        for val in rows:
            # storing current date and time in a
            # variable
            current_date_time = datetime.now()
            val.insert(0, current_date_time)

            # writing the data in csv file
            file_write.writerow(val)
