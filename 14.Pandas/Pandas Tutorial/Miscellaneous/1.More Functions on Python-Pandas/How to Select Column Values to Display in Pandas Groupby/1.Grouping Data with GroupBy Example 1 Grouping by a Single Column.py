import pandas as pd

# Sample data
data = {
    'Animal': ['Cheetah', 'Cheetah', 'Lion', 'Lion', 'Tiger', 'Tiger'],
    'Max Speed': [100, 95, 80, 85, 65, 70]
}

df = pd.DataFrame(data)

# Group by 'Animal' and calculate mean speed
mean_speed = df.groupby('Animal').mean()
print(mean_speed)
