# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'X': [1, 2, 3, 4, 5],
	'Y': [2, 4, 6, 10, 15]
})

# plotting a line graph
print("Line graph: ")
plt.plot(df["X"], df["Y"])
plt.show()

# plotting a scatter plot
print("Scatter Plot: ")
plt.scatter(df["X"], df["Y"])
plt.show()
