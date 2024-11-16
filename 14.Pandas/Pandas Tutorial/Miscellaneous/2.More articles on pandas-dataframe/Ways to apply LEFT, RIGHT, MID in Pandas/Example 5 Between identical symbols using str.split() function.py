# importing pandas library
import pandas as pd

# creating and initializing a list
Cars = ['M3-1906-BMW','M5-2096-Audi',
		'M11-3096-Volkswagen','M9-4096-Datsun',
		'M8-5096-Toyota','M23-6096-Maruti Suzuki']

# creating a pandas dataframe
df = pd.DataFrame(Cars, columns= ['Model_name'])

# Extracting characters between symbol "-"
# using srt.strip() and str[1]
# and storing result to 'Before_symbol'
BetweenTwoSymbols = df['Model_name'].str.split('-').str[1]

print (BetweenTwoSymbols)
