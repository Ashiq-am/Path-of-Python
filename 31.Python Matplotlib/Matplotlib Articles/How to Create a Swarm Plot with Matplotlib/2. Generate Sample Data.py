# Create a sample dataset
np.random.seed(0)
categories = ['A', 'B', 'C']
data = {
    'Category': np.random.choice(categories, size=150),
    'Value': np.random.randn(150)
}
df = pd.DataFrame(data)
