import matplotlib.pyplot as plt

# Using a inbuilt style to change
# the look and feel of the plot
plt.style.use("fivethirtyeight")

# setting figure size to 12, 10
plt.figure(figsize=(12, 10))

# Labelling the axes and setting
# a title
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Values of 'A' and Rolling Mean (2) Plot")

# plotting the "A" column and "A" column
# of Rolling Dataframe (window_size = 20)
plt.plot(dataframe["A"])
plt.plot(dataframe.rolling(
window=2, min_periods=1).mean()["A"])
