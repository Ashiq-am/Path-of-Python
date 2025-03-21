# importing the library
import pandas as pd

# Dataframe
df = pd.DataFrame({'team': ['Team 1', 'Team 1', 'Team 2',
							'Team 3', 'Team 2', 'Team 3'],
				'Subject': ['Math', 'Science', 'Science',
							'Math', 'Science', 'Math'],
				'points': [10, 8, 10, 6, 6, 5]})

# Dropping the team 1
df = df[df["team"].str.contains("Team 1") == False]

df
