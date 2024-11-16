# import pandas library
import pandas as pd


# This function take a dataframe
# as a parameter and returning list
# of column names whose contents
# are duplicates.
def getDuplicateColumns(df):
    # Create an empty set
    duplicateColumnNames = set()

    # Iterate through all the columns
    # of dataframe
    for x in range(df.shape[1]):

        # Take column at xth index.
        col = df.iloc[:, x]

        # Iterate through all the columns in
        # DataFrame from (x + 1)th index to
        # last index
        for y in range(x + 1, df.shape[1]):

            # Take column at yth index.
            otherCol = df.iloc[:, y]

            # Check if two columns at x & y
            # index are equal or not,
            # if equal then adding
            # to the set
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])

            # Return list of unique column names
    # whose contents are duplicates.
    return list(duplicateColumnNames)


# Driver code
if __name__ == "__main__":
    # List of Tuples
    students = [
        ('Ankit', 34, 'Uttar pradesh', 34),
        ('Riti', 30, 'Delhi', 30),
        ('Aadi', 16, 'Delhi', 16),
        ('Riti', 30, 'Delhi', 30),
        ('Riti', 30, 'Delhi', 30),
        ('Riti', 30, 'Mumbai', 30),
        ('Ankita', 40, 'Bihar', 40),
        ('Sachin', 30, 'Delhi', 30)
    ]

    # Create a DataFrame object
    df = pd.DataFrame(students,
                      columns=['Name', 'Age', 'Domicile', 'Marks'])

    # Dropping duplicate columns
    rslt_df = df.drop(columns=getDuplicateColumns(df))

    print("Resultant Dataframe :")

    # Show the dataframe
    rslt_df
