import pandas as pd


def weighted_average_of_group(values, weights, item):
	return (values * weights).groupby(item).sum() / weights.groupby(item).sum()


# creating a datafrane to represent different items
# and their corresponding weight and value
dataframe = pd.DataFrame({'item_name': ['Chocolate', 'Chocolate', 'Chocolate',
										'Biscuit', 'Biscuit', 'Biscuit',
										'IceCream', 'IceCream', 'IceCream'],
						'value': [90, 50, 86, 87, 42, 48, 68, 92, 102],
						'weight': [4, 2, 3, 5, 6, 5, 3, 7, 5]})

# Finding grouped average of group
weighted_average_of_group(values=dataframe.value,
						weights=dataframe.weight, item=dataframe.item_name)
