import pandas as pd

# Create a dictionary of students
students = {
    'Name': ['Lisa', 'Kate', 'Ben', 'Kim', 'Josh',
             'Alex', 'Evan', 'Greg', 'Sam', 'Ella'],
    'ID': ['001', '002', '003', '004', '005', '006',
           '007', '008', '009', '010'],
    'Grade': ['A', 'A', 'C', 'B', 'B', 'B', 'C',
              'A', 'A', 'A'],

    'Category': [2, 3, 1, 3, 2, 3, 3, 1, 2, 1]
}

# Create dataframe from students dictionary
df = pd.DataFrame(students)

# view the dataframe
df
