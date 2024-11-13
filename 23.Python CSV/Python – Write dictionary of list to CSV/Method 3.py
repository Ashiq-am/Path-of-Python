# import the csv package
import csv

# create a csv file with desired name
# and store it in a variable
with open('test.csv', 'w') as testfile:
    # store the desired header row as a list
    # and store it in a variable
    fieldnames = ['first_field', 'second_field', 'third_field']

    # pass the created csv file and the header
    # rows to the Dictwriter function
    writer = csv.DictWriter(testfile, fieldnames=fieldnames)

    # Now call the writeheader function,
    # this will write the specified rows as
    # headers of the csv file
    writer.writeheader()
