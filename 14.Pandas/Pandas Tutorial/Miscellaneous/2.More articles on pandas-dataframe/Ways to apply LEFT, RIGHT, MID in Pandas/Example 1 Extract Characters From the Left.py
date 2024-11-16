# importing pandas library
import pandas as pd

# creating and initializing a list
Cars = ['1000-BMW','2000-Audi','3000-Volkswagen',
		'4000-Datsun','5000-Toyota','6000-Maruti Suzuki']

# creating a pandas dataframe
df = pd.DataFrame(Cars, columns= ['Model_name'])

# Extracting characters from right side
# using slicing and storing result in
# 'Left'
Left = df['Model_name'].str[:4]

print(Left)
