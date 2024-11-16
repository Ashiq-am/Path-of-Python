import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'Score': [85, 72, 90, 60, 78]})

# Use a lambda function with the apply function to classify scores
df['Classification'] = df['Score'].apply(lambda x: 'Pass' if x >= 75 else 'Fail')

print(df)
