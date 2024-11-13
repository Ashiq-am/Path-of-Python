# This code fix ValueError: Trailing data
import pandas as pd

df = pd.read_json('sample_json.json')
print(df.head())
