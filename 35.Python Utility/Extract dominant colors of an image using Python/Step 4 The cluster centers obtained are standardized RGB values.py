cluster_centers, _ = kmeans(batman_df[['scaled_color_red',
									'scaled_color_blue',
									'scaled_color_green']], 3)

dominant_colors = []

# Get standard deviations of each color
red_std, green_std, blue_std = batman_df[['red',
										'green',
										'blue']].std()

for cluster_center in cluster_centers:
	red_scaled, green_scaled, blue_scaled = cluster_center

	# Convert each standardized value to scaled value
	dominant_colors.append((
		red_scaled * red_std / 255,
		green_scaled * green_std / 255,
		blue_scaled * blue_std / 255
	))

# Display colors of cluster centers
plt.imshow([dominant_colors])
plt.show()
