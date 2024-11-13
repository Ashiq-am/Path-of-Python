# Program to write a dictionary of list to csv
import csv

# dictionary of list
d = {"key1": ['a', 'b', 'c'],
     "key2": ['d', 'e', 'f'],
     "key3": ['g', 'h', 'i']}

# writing to csv file
with open("test.csv", "w") as outfile:
    # creating a csv writer object
    writerfile = csv.writer(outfile)

    # writing dictionary keys as headings of csv
    writerfile.writerow(d.keys())

    # writing list of dictionary
    writerfile.writerows(zip(*d.values()))
