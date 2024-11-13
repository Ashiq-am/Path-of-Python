# Generate sample data
data = np.random.rand(10, 10)
df = pd.DataFrame(data, columns=[f'Col{i}' for i in range(1, 11)])
