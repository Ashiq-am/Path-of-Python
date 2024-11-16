import pandas as pd

num = {'data': [1,"hjghjd",3,"jxsh"]}
df = pd.DataFrame(num)

# this will convert non-numeric
# values into NaN values
df = pd.to_numeric(df["data"], errors='coerce')

df
