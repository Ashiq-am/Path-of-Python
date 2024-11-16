# Creating the MultiIndex
midx = pd.MultiIndex.from_product([Name, Price],
					names =['Name', 'Price'])

# Print the MultiIndex
print(midx)
