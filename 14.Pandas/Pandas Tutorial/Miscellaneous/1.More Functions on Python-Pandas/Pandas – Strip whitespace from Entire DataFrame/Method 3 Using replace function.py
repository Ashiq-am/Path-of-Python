# importing library
import pandas as pd

# Creating dataframe
df = pd.DataFrame({'Name' : [' Sunny','Bunny','Ginny ',' Binny ',' Chinni','Minni'],
					'Age' : [23,44,23,54,22,11],
					'Blood Group' : [' A+',' B+','O+','O-',' A-','B-'],
				'Gender' : [' M',' M','F','F','F',' F']
				})

# As dataset having lot of extra spaces in cell so lets remove them using strip() function
df['Names'].str.replace(' ', '')
df['Bolld Group'].str.replace(' ', '')
df['Gender'].str.replace(' ', '')

# Printing dataframe
print(df)
