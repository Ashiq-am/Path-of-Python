# Set figure size (width, height) in inches
fig, ax = plt.subplots(figsize = ( 5 , 3 ))

# Plot the scatterplot
sns.scatterplot( ax = ax , x = "total_bill" , y = "tip" , data = tips )

# Set label for x-axis
ax.set_xlabel( "Total Bill (USD)" , size = 12 )

# Set label for y-axis
ax.set_ylabel( "Tips (USD)" , size = 12 )

# Set title for plot
ax.set_title( "Bill vs Tips" , size = 24 )

# Display figure
plt.show()
