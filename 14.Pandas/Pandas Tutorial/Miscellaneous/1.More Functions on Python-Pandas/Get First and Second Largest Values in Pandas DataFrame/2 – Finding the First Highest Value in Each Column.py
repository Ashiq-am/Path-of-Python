import pandas as pd

# Sample DataFrame
data = {
    'Scores': [85, 92, 75, 91, 88],
    'Age': ['Arun', 'Vikas', 'Varun', 'Yogesh', 'Satyam'],
    'Profit': [50.44, 69.33, 34.14, 56.13, -20.02]
}
df = pd.DataFrame(data)

# Get the highest value
highest_value = df.max()
print("Highest Value:")
print(highest_value)
