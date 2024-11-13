# import necessary libraries
import matplotlib.pyplot as plt

mens_age = 18, 19, 20, 21, 22, 23, 24, 25, 26, 27
female_age = 22, 28, 30, 30, 12, 33, 41, 22, 43, 18

plt.hist([mens_age, female_age], color=[
		'Black', 'Red'], label=['Male', 'Female'])
plt.xlabel('Age')
plt.ylabel('Person Count')
plt.legend()
plt.show()
