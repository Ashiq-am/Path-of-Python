# importing pandas library
import pandas as pd

# creating and initializing a list
Cars = ['ID-11111-BMW','ID-22222-Volkswagen',
		'ID-33333-Toyota','ID-44444-Hyundai ',
		'ID-55555-Datsun','ID-66666-Mercedes']

# creating a pandas dataframe
df = pd.DataFrame(Cars, columns= ['Model_name'])

# Extracting characters from Middle using
# slicing and storing result in 'Mid'
Mid = df['Model_name'].str[4:8]

print (Mid)
