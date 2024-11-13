import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['file.csv']))
print(df)
