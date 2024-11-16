import pandas as pd


# initialize country
country = ["India", "Australia", "Pak", "Sri Lanka",
		"England", "Bangladesh"]

# perform period_range() function
match_date = pd.period_range('8/1/2020', '8/6/2020', freq='D')

# genrates dataframes
df = pd.DataFrame(country, index=match_date, columns=['Country'])

df
