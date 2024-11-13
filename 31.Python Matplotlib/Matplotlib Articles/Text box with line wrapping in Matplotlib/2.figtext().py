import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [50, 40, 40, 80, 20]
y2 = [80, 20, 20, 50, 60]

plt.plot(x, y, 'g', label='BMW', linewidth=5)
plt.plot(x, y2, 'c', label='Ferrari', linewidth=5)

plt.title('Car details in line plot')
plt.ylabel('Distance in kms')
plt.xlabel('Days')
plt.figtext(0.4, 0.2, "Ferrari")
plt.figtext(0.35, 0.4, "BMW")
plt.legend()
