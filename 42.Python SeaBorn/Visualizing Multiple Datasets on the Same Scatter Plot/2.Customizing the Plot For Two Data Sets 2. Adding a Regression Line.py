# Adding regression lines
sns.lmplot(data=combined_data, x='x', y='y', hue='label', markers=['o', 's'], palette=['blue', 'red'], height=6, aspect=1.5)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Regression Lines')

# Display the plot
plt.show()
