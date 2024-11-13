# Set figure size
sns.set( rc = {'figure.figsize' : ( 20, 20 ),
			'axes.labelsize' : 12 })

# Plot scatter plot
g = sns.relplot(data = tips , x = "total_bill" ,
				y = "tip" , col = "time" ,
				hue = "day" , style = "day" ,
				kind = "scatter" )

# Title for the complete figure
g.fig.suptitle("Tips by time of day" ,
			fontsize = 'x-large' ,
			fontweight = 'bold' )

# Adjust subplots so that titles don't overlap
g.fig.subplots_adjust( top = 0.85 )

# Set x-axis and y-axis labels
g.set_axis_labels( "Tip" , "Total Bill (USD)" )

# Display the figure
plt.show()
