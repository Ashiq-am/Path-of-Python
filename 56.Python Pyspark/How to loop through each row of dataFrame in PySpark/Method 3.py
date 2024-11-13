pd_df = df.toPandas()

# looping through each row using iterrows()
# used to iterate over dataframe rows as index,
# series pair
for index, row in pd_df.iterrows():
    # while looping through each row
    # printing the Id, Name and Salary
    # by passing index instead of Name
    # of the column
    print(row[0], row[1], " ", row[3])
