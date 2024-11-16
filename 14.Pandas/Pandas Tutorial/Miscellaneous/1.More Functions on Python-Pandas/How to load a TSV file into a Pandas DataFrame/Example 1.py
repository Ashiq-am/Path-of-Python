import pandas as pd

# Data.tsv is stored locally in the
# same directory as of this python file
df = pd.read_csv('data.tsv',sep = '\t')
df
