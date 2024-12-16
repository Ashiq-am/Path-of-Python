import numpy as np

# Combine 'Age' and 'Salary' into a new column, but only for those with Age > 30
df['Age and Salary'] = np.where(df['Age'] > 30, df['Age'] + df['Salary'], 0)

# Display the updated DataFrame
print(df)