# Splitting the plot into (1,2) subplots
# and initializing them using fig and ax
# variables
fig, ax = plt.subplots(nrows=1, ncols=2,
					figsize=(15, 6))

# Using Seaborn Library for Box Plot
sns.boxplot(dataframe['Year'],
			dataframe["A"], ax=ax[0])

# Defining the title and axes names
ax[0].set_title('Year-wise Box Plot for A',
				fontsize=20, loc='center')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('"A" values')

# Using Seaborn Library for Box Plot
sns.boxplot(dataframe['Month'],
			dataframe["A"], ax=ax[1])

# Defining the title and axes names
ax[1].set_title('Month-wise Box Plot for A',
				fontsize=20, loc='center')
ax[1].set_xlabel('Month')
ax[1].set_ylabel('"A" values')

# rotate the ticks and right align them
fig.autofmt_xdate()
