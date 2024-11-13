# Create a basic plot
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Sine Wave')
line2, = ax.plot(x, y2, label='Cosine Wave')

# Add the first legend with customizations
first_legend = ax.legend(handles=[line1], loc='upper right', fontsize='small', frameon=True, shadow=True, borderpad=1)

# Add the second legend with customizations
second_legend = plt.legend(handles=[line2], loc='lower right', fontsize='small', frameon=True, shadow=True, borderpad=1)

# Manually add the first legend back to the plot
ax.add_artist(first_legend)

plt.title('Plot with Customized Legends')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
