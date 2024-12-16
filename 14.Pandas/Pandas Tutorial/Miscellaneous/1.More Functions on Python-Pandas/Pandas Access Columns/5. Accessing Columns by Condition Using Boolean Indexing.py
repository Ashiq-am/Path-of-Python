# Access the 'Salary' column where 'Age' is greater than 25
high_salary = df[df['Age'] > 25]['Salary']
print(high_salary)