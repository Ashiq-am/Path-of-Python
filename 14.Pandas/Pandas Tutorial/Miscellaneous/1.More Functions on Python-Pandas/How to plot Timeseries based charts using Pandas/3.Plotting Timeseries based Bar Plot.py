import matplotlib.pyplot as plt

# Using a inbuilt style to change
# the look and feel of the plot
plt.style.use("fivethirtyeight")

# setting figure size to 12, 10
plt.figure(figsize=(15, 10))

# Labelling the axes and setting a
# title
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Bar Plot of 'A'")

# plotting the "A" column alone
plt.bar(dataframe.index, dataframe["A"], width=5)
