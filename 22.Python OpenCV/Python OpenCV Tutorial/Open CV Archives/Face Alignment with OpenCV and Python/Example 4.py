# Calculate the length of all the edges
def trignometry_for_distance(a, b):
	return math.sqrt(((b[0] - a[0]) * (b[0] - a[0])) \
					+ ((b[1] - a[1]) * (b[1] - a[1])))
