# Create a sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'value': np.random.randn(1000)  # 1000 random numbers from a normal distribution
})
