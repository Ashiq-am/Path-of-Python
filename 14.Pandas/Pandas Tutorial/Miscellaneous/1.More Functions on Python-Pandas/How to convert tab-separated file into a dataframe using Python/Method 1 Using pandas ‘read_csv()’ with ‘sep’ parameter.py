import pandas as pd
file_path = "file.tsv"
df = pd.read_csv(file_path,sep='\t')
df.head()
