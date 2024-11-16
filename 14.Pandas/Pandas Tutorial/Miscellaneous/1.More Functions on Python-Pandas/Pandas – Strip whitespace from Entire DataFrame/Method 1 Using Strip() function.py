# importing library
import pandas as pd

# Creating dataframe
df = pd.DataFrame({'Names' : [' Sunny','Bunny','Ginny ',' Binny ',' Chinni','Minni'],
					'Age' : [23,44,23,54,22,11],
					'Blood Group' : [' A+',' B+','O+','O-',' A-','B-'],
				'Gender' : [' M',' M','F','F','F',' F']
				})

# As dataset having lot of extra spaces in cell so lets remove them using strip() function
df['Names'].str.strip()
df['Bolld Group'].str.strip()
df['Gender'].str.strip()

# Printing dataframe
print(df)
