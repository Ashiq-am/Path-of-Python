# Importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Setting the data
x = ["Student1", "Student2"]
y = [80, 68]

# setting the dimensions of the plot
fig, ax = plt.subplots(figsize=(6, 6))

# drawing the plot
sns.barplot(x, y, ax=ax)
plt.show()
