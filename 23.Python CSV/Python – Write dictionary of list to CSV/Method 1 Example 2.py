# create a dictionary of list
test = {'Age': [52, 24, 31, 47, 51, 61],
        'Sex': ['F', 'M', 'M', 'F', 'F', 'M'],
        'height': [143, 163, 144, 154, 174, 177],
        'weight': [77, 66, 59, 53, 71, 63], }

# create a csv file called test.csv and
# store it a temp variable as outfile
with open("test.csv", "w") as outfile:
    # pass the csv file to csv.writer.
    writer = csv.writer(outfile)

    # convert the dictionary keys to a list
    key_list = list(test.keys())

    # find th length of the key_list
    limit = len(key_list)

    # the length of the keys corrsponds to
    # no. of. columns.
    writer.writerow(test.keys())

    # iterate each column and assign the
    # corresponding values to the column
    for i in range(limit):
        writer.writerow([test[x][i] for x in key_list])
