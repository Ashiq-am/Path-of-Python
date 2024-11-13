# create a dictionary of list
test = {'Age': [52, 24, 31, 47, 51, 61],
        'Sex': ['F', 'M', 'M', 'F', 'F', 'M'],
        'height': [143, 163, 144, 154, 174, 177],
        'weight': [77, 66, 59, 53, 71, 63], }

# create a csv file test.csv and store
# it in a variable as outfile
with open("test.csv", "w") as outfile:
    # pass the csv file to csv.writer function.
    writer = csv.writer(outfile)

    # pass the dictionary keys to writerow
    # function to frame the columns of the csv file
    writer.writerow(test.keys())

    # make use of writerows function to append
    # the remaining values to the corresponding
    # columns using zip function.
    writer.writerows(zip(*test.values()))
