#Get current axis
ax = plt.gca()

# line plot for math marks
df.plot(kind = 'line',
		x = 'name',
		y = 'math_marks',
		color = 'green',ax = ax)

# line plot for physics marks
df.plot(kind = 'line',x = 'name',
		y = 'physics_marks',
		color = 'blue',ax = ax)

# line plot for chemistry marks
df.plot(kind = 'line',x = 'name',
		y = 'chem_marks',
		color = 'black',ax = ax)

# set the title
plt.title('LinePlots')

# show the plot
plt.show()
