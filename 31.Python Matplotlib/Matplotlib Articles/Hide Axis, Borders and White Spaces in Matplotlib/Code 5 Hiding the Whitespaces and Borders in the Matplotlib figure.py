# code
import numpy as np
import matplotlib.pyplot as plt

# Marks of RAM in different subjects out of 100.
x = ['Science', 'Maths', 'English', 'History', 'Geography']
y = [75, 85, 88, 78, 74]

fig = plt.bar(x, y)
plt.xlabel("Subject")
plt.ylabel("Ram's marks out of 100")
plt.axis('off')
# Command used for hiding whitespaces and border.
plt.savefig('image.png', bbox_inches='tight', pad_inches=0)

plt.show()
