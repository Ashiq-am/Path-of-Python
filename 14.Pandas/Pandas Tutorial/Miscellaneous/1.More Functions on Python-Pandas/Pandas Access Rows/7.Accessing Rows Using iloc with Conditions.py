# Access the first row where 'Age' is greater than 25
filtered_row = df[df['Age'] > 25].iloc[0]
print(filtered_row)