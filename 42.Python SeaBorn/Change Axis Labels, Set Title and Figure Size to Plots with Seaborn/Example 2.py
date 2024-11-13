# Set figure size (width, height) in inches
plt.figure(figsize = ( 5 , 3 ))

# Plot scatterplot
sns.scatterplot( x = "total_bill" , y = "tip" , data = tips )

# Set label for x-axis
plt.xlabel( "Total Bill (USD)" , size = 12 )

# Set label for y-axis
plt.ylabel( "Tips (USD)" , size = 12 )

# Set title for figure
plt.title( "Bill vs Tips" , size = 24 )

# Display figure
plt.show()
