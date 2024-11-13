# Create a basic plot
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Sine Wave')
line2, = ax.plot(x, y2, label='Cosine Wave')

# Add the first legend
first_legend = ax.legend(handles=[line1], loc='upper right')

# Add the second legend
second_legend = plt.legend(handles=[line2], loc='lower right')

# Manually add the first legend back to the plot
ax.add_artist(first_legend)

plt.title('Plot with Two Legends')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
