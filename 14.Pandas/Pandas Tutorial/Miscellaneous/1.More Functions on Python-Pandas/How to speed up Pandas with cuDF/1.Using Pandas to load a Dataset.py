# Loading the Dataset using Pandas Library (CPU Based)
import pandas as pd
import time


start = time.time()
df = pd.read_csv("Data.csv")
print("no. of rows in the dataset", df.shape[0])
print("no. of columns in the dataset", df.shape[1])
end = time.time()
print("CPU time= ", end-start)
