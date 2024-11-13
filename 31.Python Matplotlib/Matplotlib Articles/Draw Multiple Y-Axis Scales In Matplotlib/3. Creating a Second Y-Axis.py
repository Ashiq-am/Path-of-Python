fig, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(x, y2, 'g', label='y2 (exp(-x))')
ax2.set_ylabel('y2', color='g')
ax2.tick_params('y', colors='g')
# Display the plot
plt.title('Plotting the Second Dataset on the Second Y-Axis')
plt.show()
