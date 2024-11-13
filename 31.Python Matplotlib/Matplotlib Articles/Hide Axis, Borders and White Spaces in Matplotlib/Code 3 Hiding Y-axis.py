# Hiding Y-axis label
import numpy as np
import matplotlib.pyplot as plt

# Marks of RAM in different subjects out of 100.
x = ['Science', 'Maths', 'English', 'History', 'Geography']
y = [75, 85, 88, 78, 74]

plt.bar(x, y)
plt.xlabel("Subject")
plt.ylabel("Ram's marks out of 100")
plt.yticks([]) # Command for hiding y-axis

plt.show()
