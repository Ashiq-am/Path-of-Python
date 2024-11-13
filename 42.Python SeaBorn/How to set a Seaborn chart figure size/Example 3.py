# Importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Setting the data
x = ["Student1", "Student2"]
y = [70, 87]

# setting the dimensions of the plot
fig, ax = plt.subplots(figsize=(40, 5))

# drawing the plot
sns.boxplot(x = y)
plt.show()
