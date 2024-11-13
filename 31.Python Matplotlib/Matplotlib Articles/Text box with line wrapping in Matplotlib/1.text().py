import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [50, 40, 40, 80, 20]
y2 = [80, 20, 20, 50, 60]

plt.plot(x, y, 'g', label='BMW', linewidth=5)
plt.plot(x, y2, 'c', label='Ferrari', linewidth=5)

plt.title('Car details in line plot')
plt.ylabel('Distance in kms')
plt.xlabel('Days')

# Text on Ferrari line plot
plt.text(2.5, 23, "Ferrari")

# Text on BMW line plot
plt.text(2.5, 43, "BMW")
plt.legend()
