import pandas as pd

url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
df = pd.read_csv(url)

df_s1 = df[:5]

df_s1 = df_s1.drop(df_s1.query('sepal_length==5.0').index)

print(df_s1)
