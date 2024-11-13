# importing libraries
import matplotlib.pyplot as plt
import random

# creating the dataset
date = [i for i in range(2000, 2021)]
value = []
for i in range(21):
	value.append(random.randint(5, 15))

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Creating the scatter plot
ax.scatter(date, value)

# Highlighting for a certain period of time
ax.axvspan(2002, 2005, alpha=0.3, color="green")
plt.show()
