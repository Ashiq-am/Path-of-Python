# Let's assume a Bonus column is added
df['Bonus'] = [5000, 6000, 4000, 7000, 3500]

# Combine 'Salary' and 'Bonus' into 'Total Compensation'
df['Total Compensation'] = df['Salary'] + df['Bonus']

# Display the updated DataFrame
print(df)