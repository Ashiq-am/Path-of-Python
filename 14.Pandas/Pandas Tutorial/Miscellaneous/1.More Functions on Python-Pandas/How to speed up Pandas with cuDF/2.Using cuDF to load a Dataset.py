# Loading the Dataset using Pandas Library (GPU Based)
import cudf
import time

start = time.time()
df = cudf.read_csv("../input/data-big/Data.csv")
print("no. of rows in the dataset", df.shape[0])
print("no. of columns in the dataset", df.shape[1])
end = time.time()
print("GPU time= ", end-start)
