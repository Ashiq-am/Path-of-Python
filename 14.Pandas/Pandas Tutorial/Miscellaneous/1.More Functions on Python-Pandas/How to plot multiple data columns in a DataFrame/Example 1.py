import pandas as pd
import matplotlib.pyplot as mp

# take data
data = pd.read_csv("Bestsellers.csv")

# form dataframe
data = data.head()

df = pd.DataFrame(data, columns=["Name", "Price", "User Rating"])

# plot the dataframe
df.plot(x="Name", y=["Price", "User Rating"], kind="bar", figsize=(9, 8))

# print bar graph
mp.show()
