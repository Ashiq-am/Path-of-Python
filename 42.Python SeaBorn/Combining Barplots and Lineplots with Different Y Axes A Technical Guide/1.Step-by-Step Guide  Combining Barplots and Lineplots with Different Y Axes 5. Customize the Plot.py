# Adjust the scale of the secondary y-axis
ax2.set_ylim(400, 600)

# Customize labels
ax1.set_ylabel('Monthly Revenue ($)', fontsize=12, color='blue')
ax2.set_ylabel('Number of New Subscribers', fontsize=12, color='darkred')

# Change axis and tick colors to match the data plots
ax1.yaxis.label.set_color('blue')
ax2.yaxis.label.set_color('darkred')
ax1.tick_params(axis='y', colors='blue')
ax2.tick_params(axis='y', colors='darkred')
plt.show()
