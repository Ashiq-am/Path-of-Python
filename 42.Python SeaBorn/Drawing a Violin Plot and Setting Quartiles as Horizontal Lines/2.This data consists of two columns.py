# Sample data creation
np.random.seed(10)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=200),
    'Values': np.random.randn(200)
})
