# Creating a sample wide DataFrame
dates = pd.date_range('2024-01-01', periods=10)
data = {
    'Series_A': np.random.randint(10, 50, size=10),
    'Series_B': np.random.randint(20, 60, size=10),
    'Series_C': np.random.randint(30, 70, size=10)
}
df = pd.DataFrame(data, index=dates)
print(df)
