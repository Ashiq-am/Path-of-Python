# Import pandas library
import pandas as pd

# List of tuples
students = [('Ankit', 23, 'Delhi', 'A'),
            ('Swapnil', 22, 'Delhi', 'B'),
            ('Aman', 22, 'Dehradun', 'A'),
            ('Jiten', 22, 'Delhi', 'A'),
            ('Jeet', 21, 'Mumbai', 'B')
            ]

# Creating Dataframe object
df = pd.DataFrame(students, columns=['Name', 'Age', 'City', 'Section'])


# This function will return a list of
# positions where element exists
# in the dataframe.
def getIndexes(dfObj, value):
    # Empty list
    listOfPos = []

    # isin() method will return a dataframe with
    # boolean values, True at the positions
    # where element exists
    result = dfObj.isin([value])

    # any() method will return
    # a boolean series
    seriesObj = result.any()

    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)

    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)

        for row in rows:
            listOfPos.append((row, col))

        # This list contains a list tuples with
    # the index of element in the dataframe
    return listOfPos


# Calling getIndexes() function to get
# the index positions of all occurrences
# of 22 in the dataframe
listOfPositions = getIndexes(df, 22)

print('Index positions of 22 in Dataframe : ')

# Printing the position
for i in range(len(listOfPositions)):
    print(listOfPositions[i])
