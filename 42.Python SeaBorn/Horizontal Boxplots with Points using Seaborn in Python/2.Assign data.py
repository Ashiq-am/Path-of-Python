# To avoid changing values everytime you run the cell
np.random.seed(42)

# Creating Data
df = pd.DataFrame({
	'Ice-cream': np.random.normal(40, 15, 100),
	'Chocolate': np.random.normal(60, 10, 100),
	'Cakes': np.random.normal(80, 5, 100)
})

# Display data
print(df)
