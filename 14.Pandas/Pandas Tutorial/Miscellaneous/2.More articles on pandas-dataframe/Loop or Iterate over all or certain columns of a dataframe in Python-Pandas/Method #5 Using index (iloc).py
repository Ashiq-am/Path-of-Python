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

# Iterate over the index range from
# 0 to max number of columns in dataframe
for index in range(stu_df.shape[1]):
    print('Column Number : ', index)

    # Select column by index position using iloc[]
    columnSeriesObj = stu_df.iloc[:, index]
    print('Column Contents : ', columnSeriesObj.values)
