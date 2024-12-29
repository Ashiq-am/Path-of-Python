import pandas as pd

# Sample student data
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 42, 78],
    'Subject': ['Math', 'Science', 'English']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter rows with Marks greater than 75 using itertuples
print("Students scoring more than 75 marks:")
for row in df.itertuples(name='Pandas'):
    if row.Marks > 75:  # 'Marks' is at index 1 in the tuple
        print(f"Student: {row.Student}, Subject: {row[2]}")