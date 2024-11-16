# import pandas library
import pandas as pd

# dictionary with list object in values
details = {
    'Name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
    'Age': [23, 21, 22, 21],
    'University': ['BHU', 'JNU', 'DU', 'BHU'],
}

# creating a Dataframe object
df = pd.DataFrame(details, columns=['Name', 'Age', 'University'], index=['a', 'b', 'c', 'd'])

# Get the number of rows and columns
rows = len(df.axes[0])
cols = len(df.axes[1])

# Print the number of rows and columns
print("Number of Rows: " + str(rows))
print("Number of Columns: " + str(cols))
