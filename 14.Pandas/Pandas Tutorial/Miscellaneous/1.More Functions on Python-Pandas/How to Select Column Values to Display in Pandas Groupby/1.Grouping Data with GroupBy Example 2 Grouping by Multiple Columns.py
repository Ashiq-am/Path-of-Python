import pandas as pd

# Sample data with multiple columns
data = {
    'Animal': ['Cheetah', 'Cheetah', 'Lion', 'Lion', 'Tiger', 'Tiger'],
    'Max Speed': [100, 95, 80, 85, 65, 70],
    'Color': ['Yellow', 'Yellow', 'Tan', 'Tan', 'Orange', 'Orange']
}

df = pd.DataFrame(data)

# Group by 'Animal' and 'Color', and calculate the sum
grouped = df.groupby(['Animal', 'Color']).sum()
print(grouped)
