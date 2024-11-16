import pandas as pd

# List of Tuples
students = [('Ankit', 22, 'A'),
            ('Swapnil', 22, 'B'),
            ('Priya', 22, 'B'),
            ('Shivangi', 22, 'B'),
            ]

# Create a DataFrame object
stu_df = pd.DataFrame(students, columns=['Name', 'Age', 'Section'],
                      index=['1', '2', '3', '4'])

# Iterate over the sequence of column names
# in reverse order
for column in reversed(stu_df.columns):
    # Select column contents by column
    # name using [] operator
    columnSeriesObj = stu_df[column]
    print('Colunm Name : ', column)
    print('Column Contents : ', columnSeriesObj.values)
