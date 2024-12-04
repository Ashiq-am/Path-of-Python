import pandas as pd

with open('df.pkl', 'rb') as file:
    df = pd.read_pickle(file)