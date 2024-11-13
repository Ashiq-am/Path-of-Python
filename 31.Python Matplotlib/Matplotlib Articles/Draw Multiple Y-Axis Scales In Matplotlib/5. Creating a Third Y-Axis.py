fig, ax3 = plt.subplots(figsize=(8, 6))
ax3.plot(x, y3, 'r', label='y3 (100*cos(x))')
ax3.set_ylabel('y3', color='r')
ax3.tick_params('y', colors='r')
# Display the plot
plt.title('Plotting the third Dataset on the third Y-Axis')
plt.show()
