import pandas as pd
df = pd.DataFrame({"values":["A","BB"]})
df['padded_values'] = df['values'].str.pad(width=5, side='right', fillchar='0')
print(df)
