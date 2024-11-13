# set figure size
plt.figure( figsize = ( 12, 5))

# plot a simple time series plot
# using seaborn.lineplot()
sns.lineplot( x = 'Date',
			y = 'Births',
			data = data,
			label = 'DailyBirths')

plt.xlabel( 'Months of the year 1959')

# setting customized ticklabels for x axis
pos = [ '1959-01-01', '1959-02-01', '1959-03-01', '1959-04-01',
	'1959-05-01', '1959-06-01', '1959-07-01', '1959-08-01',
	'1959-09-01', '1959-10-01', '1959-11-01', '1959-12-01']

lab = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
	'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

plt.xticks( pos, lab)

plt.ylabel('Female Births')
