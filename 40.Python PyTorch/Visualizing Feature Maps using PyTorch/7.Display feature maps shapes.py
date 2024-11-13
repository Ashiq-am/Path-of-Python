# Display feature maps shapes
print("\nFeature maps shape")
for feature_map in feature_maps:
	print(feature_map.shape)

# Process and visualize feature maps
processed_feature_maps = [] # List to store processed feature maps
for feature_map in feature_maps:
	feature_map = feature_map.squeeze(0) # Remove the batch dimension
	mean_feature_map = torch.sum(feature_map, 0) / feature_map.shape[0] # Compute mean across channels
	processed_feature_maps.append(mean_feature_map.data.cpu().numpy())
