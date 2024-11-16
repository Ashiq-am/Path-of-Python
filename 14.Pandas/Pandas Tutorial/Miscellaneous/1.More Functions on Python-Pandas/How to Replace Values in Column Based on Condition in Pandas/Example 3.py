# Importing the libraries
import pandas as pd
import numpy as np

# data
student = {
	'Name': ['John', 'Jay', 'sachin', 'Geetha', 'Amutha', 'ganesh'],
	'gender': ['male', 'male', 'male', 'female', 'female', 'male'],
	'math score': [50, 100, 70, 80, 75, 40],
	'test preparation': ['none', 'completed', 'none', 'completed',
						'completed', 'none'],
}

# creating a Dataframe object
df = pd.DataFrame(student)

# Applying the condition
df['gender'].mask(df['gender'] == 'female', 0, inplace=True)

# Try this too
#df['math score'].mask(df['math score'] >=60 ,'good', inplace=True)
