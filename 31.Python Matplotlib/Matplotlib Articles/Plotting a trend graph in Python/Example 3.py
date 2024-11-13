# import the library
import matplotlib.pyplot as plt


# Creation of Data
x1 = ['math', 'english', 'science', 'Hindi', 'social studies']
y1 = [92, 54, 63, 75, 53]
y2 = [86, 44, 65, 98, 85]

# Plotting the Data
plt.plot(x1, y1, label='Semester1')
plt.plot(x1, y2, label='semester2')

plt.xlabel('subjects')
plt.ylabel('marks')
plt.title("marks obtained in 2010")

plt.plot(y1, 'o:g', linestyle='--', linewidth='8')
plt.plot(y2, 'o:g', linestyle=':', linewidth='8')

plt.legend()
