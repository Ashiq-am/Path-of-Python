import pandas as pd

# Create a list of names for each row
d = {'Names': [['Alice', 'Bob', 'Charlie'], ['David', 'Eve'], ['Frank']]}
df = pd.DataFrame(d)
print(df)
