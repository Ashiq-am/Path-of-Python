# Creating a sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'] * 10,
    'Values': [10, 20, 15, 30, 25, 11, 18, 13, 35, 22, 9, 21, 14, 31, 23,
               12, 19, 16, 28, 24, 8, 17, 14, 29, 26]
}
df = pd.DataFrame(data)
