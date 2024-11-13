# import the csv package
import csv

# create a file called test.csv
# and store it in a temporary variable
with open('test.csv', 'w') as testfile:
    # pass the temp variable to csv.writer
    # function
    csvwriter = csv.writer(testfile)

    # pass the row values to be stored in
    # different rows
    csvwriter.writerows([['row1'], ['row2'], ['row3'],
                         ['row4'], ['row5'], ['row6']])
