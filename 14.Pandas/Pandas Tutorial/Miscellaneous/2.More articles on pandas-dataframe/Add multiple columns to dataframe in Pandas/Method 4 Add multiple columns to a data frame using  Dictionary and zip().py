# importing pandas library
import pandas as pd

# creating and initializing a nested list
students = [['jackma', 34, 'Sydeny', 'Australia'],
            ['Ritika', 30, 'Delhi', 'India'],
            ['Vansh', 31, 'Delhi', 'India'],
            ['Nany', 32, 'Tokyo', 'Japan'],
            ['May', 16, 'New York', 'US'],
            ['Michael', 17, 'las vegas', 'US']]

# Create a DataFrame object
df = pd.DataFrame(students,
                  columns=['Name', 'Age', 'City', 'Country'],
                  index=['a', 'b', 'c', 'd', 'e', 'f'])

# creating 2 lists 'ids' and 'marks'
ids = [11, 12, 13, 14, 15, 16]
marks = [85, 41, 77, 57, 20, 95, 96]

# Creating columns 'ID' and 'Uni_marks'
# using Dictionary and zip()
df['ID'] = dict(zip(ids, df['Name']))
df['Uni_Marks'] = dict(zip(marks, df['Name']))

# Displaying the Data frame
df
