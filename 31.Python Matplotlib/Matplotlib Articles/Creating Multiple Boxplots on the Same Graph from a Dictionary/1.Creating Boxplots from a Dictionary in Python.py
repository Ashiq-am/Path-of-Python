# Importing libraries
import matplotlib.pyplot as plt

# Sample data
data_dict = {
    'Group A': [23, 45, 56, 67, 34, 89, 45],
    'Group B': [34, 56, 78, 12, 45, 67, 89],
    'Group C': [13, 24, 35, 46, 57, 68, 79]
}

# Creating the boxplot
plt.boxplot(data_dict.values(), labels=data_dict.keys())
plt.show()
