# Set the size of the plot
plt.figure(figsize=(10, 6))

# Create the histogram
sns.histplot(data=tips, x='total_bill', hue='sex', multiple='stack')

# Add title and labels
plt.title('Total Bill Distribution by Gender')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')

# Display the plot
plt.show()
