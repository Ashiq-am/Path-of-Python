import pandas as pd

# Creating dataframe
df = pd.DataFrame({"CoronaData": data})

# Naming the coloumns
df.index = ['TotalCases', ' Deaths', 'Recovered']
