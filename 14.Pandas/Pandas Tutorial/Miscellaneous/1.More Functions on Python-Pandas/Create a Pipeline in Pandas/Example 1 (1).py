# function to find maen
def mean_age_by_group(dataframe, col):
    # groups the data by a column and
    # returns the mean age per group
    return dataframe.groupby(col).mean()


# function to convert to uppercase
def uppercase_column_name(dataframe):
    # Converts all the column names into uppercase
    dataframe.columns = dataframe.columns.str.upper()

    # And returns them
    return dataframe
