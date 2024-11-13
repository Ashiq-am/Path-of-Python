import pandas as pd
df = pd.DataFrame({"values": ["A", "BB"]})
df['padded_values'] = df['values'].str.pad(width=5, side='left', fillchar='0')
print(df)
