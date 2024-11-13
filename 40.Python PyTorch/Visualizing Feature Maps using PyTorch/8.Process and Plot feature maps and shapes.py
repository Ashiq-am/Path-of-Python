# Display processed feature maps shapes
print("\n Processed feature maps shape")
for fm in processed_feature_maps:
	print(fm.shape)

# Plot the feature maps
fig = plt.figure(figsize=(30, 50))
for i in range(len(processed_feature_maps)):
	ax = fig.add_subplot(5, 4, i + 1)
	ax.imshow(processed_feature_maps[i])
	ax.axis("off")
	ax.set_title(layer_names[i].split('(')[0], fontsize=30)
