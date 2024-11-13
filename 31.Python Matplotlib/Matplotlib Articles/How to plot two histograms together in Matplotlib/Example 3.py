# importing libraries
import matplotlib.pyplot as plt

# giving two age groups data
age_g1 = [1, 3, 5, 10, 15, 17, 18, 16, 19, 21,
		23, 28, 30, 31, 33, 38, 32, 40, 45,
		43, 49, 55, 53, 63, 66, 85, 80, 57,
		75, 93, 95]

age_g2 = [6, 4, 15, 17, 19, 21, 28, 23, 31, 36,
		39, 32, 50, 56, 59, 74, 79, 34, 98, 97,
		95, 67, 69, 92, 45, 55, 77, 76, 85]

# plotting first histogram
plt.hist(age_g1, label='Age group1', alpha=.7, edgecolor='red')

# plotting second histogram
plt.hist(age_g2, label='Age group2', alpha=0.7, edgecolor='yellow')
plt.legend()

# Showing the plot using plt.show()
plt.show()
