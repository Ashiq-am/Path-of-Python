# applying selective search
img_lbl, regions = selectivesearch.selective_search(
	resized_image, scale=500, sigma=0.9, min_size=10)
