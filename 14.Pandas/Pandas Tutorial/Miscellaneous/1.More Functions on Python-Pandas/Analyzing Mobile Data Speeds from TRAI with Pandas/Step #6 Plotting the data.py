fig, ax = plt.subplots()

# the width of each bar
bar_width = 0.25

# opacity of each bar
opacity = 0.8

# store the positions
index = np.arange(len(final_states))

# the plt.bar() takes in the position
# of the bars, data to be plotted,
# width of each bar and some other
# optional parameters, like the opacity and colour

# plot the download bars
bar_download = plt.bar(index, final_download_speeds,
					bar_width, alpha=opacity,
					color='b', label='Download')
# plot the upload bars
bar_upload = plt.bar(index + bar_width, final_upload_speeds,
						bar_width, alpha=opacity, color='g',
											label='Upload')

# title of the graph
plt.title('Avg. Download/Upload speed for '
					+ str(CONST_OPERATOR))

# the x-axis label
plt.xlabel('States')

# the y-axis label
plt.ylabel('Average Speeds in Kbps')

# the label below each of the bars,
# corresponding to the states
plt.xticks(index + bar_width, final_states, rotation=90)

# draw the legend
plt.legend()

# make the graph layout tight
plt.tight_layout()

# show the graph
plt.show()
