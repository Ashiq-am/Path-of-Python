# creating dataset
df = pd.DataFrame({
	'Ice-cream': np.random.normal(57, 5, 100),
	'Chocolate': np.random.normal(73, 5, 100),
	'cupcake': np.random.normal(68, 8, 100),
	'jamroll': np.random.normal(37, 10, 100),
	'cake': np.random.normal(76, 5, 100),

})
df.head()
