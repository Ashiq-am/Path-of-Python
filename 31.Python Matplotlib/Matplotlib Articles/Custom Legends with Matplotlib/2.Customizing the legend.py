# importing library
import matplotlib.pyplot as plt

# plotting values
a = [1, 2, 3, 4]
b = [1, 4, 9, 16]

# PLotting using matplotlib
plt.plot(a, label="A")
plt.plot(b, label="B")

# Creating legend
# Adding the location
plt.legend(loc='center left')
