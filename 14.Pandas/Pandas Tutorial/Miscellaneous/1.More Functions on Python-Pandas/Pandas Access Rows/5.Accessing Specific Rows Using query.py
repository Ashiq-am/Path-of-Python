# Access rows where 'Age' is greater than 25 and 'Salary' is less than 60000
filtered_query = df.query('Age > 25 and Salary < 60000')
print(filtered_query)