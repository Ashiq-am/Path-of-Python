# Create a scatterplot with customizations
plt.figure(figsize=(10, 6))  # Set figure size
scatter = sns.scatterplot(x=array[:, 0], y=array[:, 1],
                          s=100,  # Marker size
                          color='purple',  # Marker color
                          marker='o',  # Marker style
                          edgecolor='black')  # Marker edge color

# Add a title and labels
plt.title("Scatterplot of Numpy Array", fontsize=16, fontweight='bold')
plt.xlabel("X Axis", fontsize=14)
plt.ylabel("Y Axis", fontsize=14)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Add a legend (if you have categories, you can specify them here)
# For demonstration, we'll add a dummy label
plt.legend(['Data Points'], loc='upper left', fontsize=12)
plt.show()
