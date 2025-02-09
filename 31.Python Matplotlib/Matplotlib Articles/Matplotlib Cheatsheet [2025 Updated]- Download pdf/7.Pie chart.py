# Data for pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Add title
plt.title("Pie Chart")

# Display the plot
plt.show()
