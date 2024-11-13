data_itr = df.rdd.toLocalIterator()

# looping thorough each row of the dataframe
for row in data_itr:
    # while looping through each row printing
    # the data of Id, Job Profile and City
    print(row["Id"], " ", row["Job Profile"], " ", row["City"])
