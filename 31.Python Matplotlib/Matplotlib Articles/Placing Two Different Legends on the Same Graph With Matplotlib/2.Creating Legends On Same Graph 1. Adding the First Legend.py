# Create a basic plot with the first legend
plt.plot(x, y1, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave')
plt.title('Plot with First Legend')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='upper right')  # Positioning the legend
plt.show()
