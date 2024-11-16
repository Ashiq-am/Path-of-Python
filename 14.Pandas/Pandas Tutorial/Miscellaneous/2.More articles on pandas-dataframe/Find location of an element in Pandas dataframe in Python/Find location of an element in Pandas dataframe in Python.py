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
df = pd.DataFrame(students, columns =['Name', 'Age', 'City', 'Section'])

df
