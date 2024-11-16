# Sorting Pandas Data frame by putting
# missing values first

# importing pandas library
import pandas as pd

# Initializing the nested list with Data set
age_list = [['Afghanistan', 1952, 8425333, 'Asia'],
			['Australia', 1957, 9712569, 'Oceania'],
			['Brazil', 1962, 76039390, 'Americas'],
			['China', 1957, 637408000, 'Asia'],
			['France', 1957, 44310863, 'Europe'],
			['India', 1952, 3.72e+08, 'Asia'],
			['United States', 1957, 0, 'Americas']]

# creating a pandas dataframe
df = pd.DataFrame(age_list, columns=['Country', 'Year',
									'Population', 'Continent'])

# Sorting by column "Population"
# by putting missing values first
df.sort_values(by=['Population'], na_position='first')
