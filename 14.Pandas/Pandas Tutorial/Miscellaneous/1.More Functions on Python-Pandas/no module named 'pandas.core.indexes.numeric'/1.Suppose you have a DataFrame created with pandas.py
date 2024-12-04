import pandas as pd
import pickle

# Using pandas 1.5.3
df = pd.DataFrame({"s": [3.3, 4.4]}, index=[2, 4])
with open("df.pkl", "wb") as f:
    pickle.dump(df, f)