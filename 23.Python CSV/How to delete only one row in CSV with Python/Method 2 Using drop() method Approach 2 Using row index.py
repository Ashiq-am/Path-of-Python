import pandas as pd

url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
df = pd.read_csv(url)

df_s = df[:5]

df_s.set_index('sepal_length', inplace=True)

df_s = df_s.drop(df_s.index[1])
#df_s.drop(df_s.index[1],inplace = True)

print(df_s)
