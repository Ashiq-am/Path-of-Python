import pandas as pd
import matplotlib.pyplot as plt

# Create a list of data
# to be represented in x-axis
subjects = [ 'Math' , 'English' , 'History ',
			'Chem' , 'Geo' , 'Physics' , 'Bio' , 'CS' ]

# Create a list of data
# to be represented in y-axis
stress = [ 9, 3 , 5 , 1 , 8 , 5 , 10 , 2 ]

# Create second list of data to be represented in y-axis
grades = [ 15, 10 , 7 , 8 , 11 , 8 , 17 , 20 ]

# Create a dataframe using the two lists
df_days_calories = pd.DataFrame(
	{ 'Subject' : subjects ,
	'Stress': stress ,
	'Grade': grades})

ax = plt.gca()

#use plot() method on the dataframe
df_days_calories.plot( x = 'Subject' , y = 'Stress', ax = ax )
df_days_calories.plot( x = 'Subject' , y = 'Grade' , ax = ax )
