# Adding a new column
df['Salary'] = [50000, 60000, 70000]

# Filtering rows based on a condition
high_salary_employees = df[df['Salary'] > 60000]
print(high_salary_employees)

# Sorting DataFrame by a column
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
