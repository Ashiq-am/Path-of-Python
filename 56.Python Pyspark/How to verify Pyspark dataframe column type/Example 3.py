print("Datatype of the columns with column names are:")

# finding datatype of all column with
# column name using for loop
for col in df.dtypes:
    # printing the column and datatype
    # of that column
    print(col[0], ",", col[1])

    # visualizing the dataframe
    df.show()
