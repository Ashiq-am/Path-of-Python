# Simple Way to Read TSV Files in Python using csv
# importing csv library
import csv

# open .tsv file
with open("GeekforGeeks.tsv") as file:
    # Passing the TSV file to
    # reader() function
    # with tab delimiter
    # This function will
    # read data from file
    tsv_file = csv.reader(file, delimiter="\t")

    # printing data line by line
    for line in tsv_file:
        print(line)
