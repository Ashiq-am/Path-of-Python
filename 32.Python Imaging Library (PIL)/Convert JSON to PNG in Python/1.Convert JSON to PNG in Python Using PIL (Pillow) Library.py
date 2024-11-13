from PIL import Image, ImageDraw, ImageFont
import json

def json_to_png(json_data, output_file):
	# Convert JSON to string
	json_str = json.dumps(json_data, indent=4)

	# Create an image with white background
	image = Image.new('RGB', (800, 600), 'white')
	draw = ImageDraw.Draw(image)

	# Set the font and size
	font = ImageFont.load_default()

	# Draw the JSON text on the image
	draw.text((10, 10), json_str, font=font, fill='black')

	# Save the image as PNG
	image.save(output_file)

# Example usage
sample_json = {"name": "John Doe", "age": 30, "city": "Example City"}
json_to_png(sample_json, "example1_output.png")
print('successfully converted JSON to PNG')
