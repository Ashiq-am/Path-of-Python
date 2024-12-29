import pandas as pd

# Sample DataFrame
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 42, 78],
    'Subject': ['Math', 'Science', 'English']
}

df = pd.DataFrame(data)

# Create a dictionary of rows
rows_dict = {}
for row in df.itertuples():  # Use plain tuples
    key = row.Index  # Use the 'Student' column as the key (index 0)
    rows_dict[key] = {
        'Marks': row.Marks,      # 'Marks' column (index 1)
        'Subject': row.Subject,    # 'Subject' column (index 2)
    }

# Print the resulting dictionary
for k,v in rows_dict.items():
    print(k,v)