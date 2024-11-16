import pandas as pd


# initialize gold price
gold_price = ["32k", "34k", "37k", "33k", "38k", "39k", "35k",
			"32k", "42k", "52k", "62k", "52k", "38k", "39k",
			"35k", "33k"]

# perform period_range() function
price_month = pd.period_range(start=pd.Period('2019Q1', freq='Q'),
							end=pd.Period('2020Q2', freq='Q'),
							freq='M')

# genrates dataframes
df = pd.DataFrame(gold_price, index=price_month, columns=['Price'])

df
