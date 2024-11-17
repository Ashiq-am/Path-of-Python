# apply non-maxima suppression to the rectangles
# this will create a single bounding box
# for each object
boxes = non_max_suppression(np.array(boxes))
