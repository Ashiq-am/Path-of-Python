# Select rectangles with
# confidence greater than threshold
(y_points, x_points) = np.where(match >= thresh)

# initialize our list of bounding boxes
boxes = list()

# store co-ordinates of each bounding box
# we'll create a new list by looping
# through each pair of points
for (x, y) in zip(x_points, y_points):
    # update our list of boxes
    boxes.append((x, y, x + W, y + H))
