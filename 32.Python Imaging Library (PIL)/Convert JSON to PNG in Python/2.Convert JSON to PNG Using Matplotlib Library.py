import matplotlib.pyplot as plt
import json

def json_to_png(json_data, output_file):
	# Convert JSON to string
	json_str = json.dumps(json_data, indent=4)

	# Create a text plot
	plt.text(0.5, 0.5, json_str, ha='center', va='center', wrap=True)

	# Remove axis ticks and labels
	plt.axis('off')

	# Save the plot as PNG
	plt.savefig(output_file, bbox_inches='tight', pad_inches=0)

# Example usage
sample_json = {"name": "John Doe", "age": 30, "city": "Example City"}
json_to_png(sample_json, "example2_output.png")
print("successfully converted JSON to PNG")
