# Creating the MultiIndex
midx = pd.MultiIndex.from_product([Snake, Variety],
					names =['Snake', 'Variety'])

# Print the MultiIndex
print(midx)
