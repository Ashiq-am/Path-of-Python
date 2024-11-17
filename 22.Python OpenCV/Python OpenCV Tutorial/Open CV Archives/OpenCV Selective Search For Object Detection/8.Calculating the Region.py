# Initialize an empty set to store selected region proposals
candidates = set()

# Iterate over all the regions detected by Selective Search
for r in regions:
	# Check if the current region's rectangle is already in candidates
	if r['rect'] in candidates:
		continue # Skip this region if it's a duplicate

	# Check if the size of the region is less than 200 pixels
	if r['size'] < 200:
		continue # Skip this region if it's too small

	# Extract the coordinates and dimensions of the region's rectangle
	x, y, w, h = r['rect']

	# Avoid division by zero by checking if height or width is zero
	if h == 0 or w == 0:
		continue # Skip this region if it has zero height or width

	# Check the aspect ratio of the region (width / height and height / width)
	if w / h > 1.2 or h / w > 1.2:
		continue # Skip this region if its aspect ratio is not within a range

	# If all conditions are met, add the region's rectangle to candidates
	candidates.add(r['rect'])
