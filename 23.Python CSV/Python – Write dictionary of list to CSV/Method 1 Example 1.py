# import the csv package
import csv

# create a csv file with desired name and
# store it in a variable
with open('test.csv', 'w') as testfile:
    # pass the the temporary variable to
    # csv.writer function
    csvwriter = csv.writer(testfile, )

    # use writerow function to insert a
    # single row to the csv file.
    csvwriter.writerow(['col1', 'col2', 'col3',
                        'col4', 'col5'])
