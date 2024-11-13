plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o')

num_xticks = len(x_values)
evenly_spaced_xticks = np.arange(num_xticks)
plt.xticks(evenly_spaced_xticks, x_values)

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Evenly Spaced X-Ticks with Adjusted Plot Size')

plt.grid(True)
plt.show()
