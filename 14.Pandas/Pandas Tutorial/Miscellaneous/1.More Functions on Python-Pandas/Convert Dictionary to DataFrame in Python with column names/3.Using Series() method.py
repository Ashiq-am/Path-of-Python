import pandas as pd

students = {"Shravan": 90, "Jeetu": 91, "Ram": 32, "Pankaj": 95}

# Convert dictionary to Series
series = pd.Series(students, name='Score')

# Convert series to DataFrame
df = pd.DataFrame(series)
df.reset_index(inplace=True)
df.columns = ['Name', 'Score']

print(df)
