# Convert the selected bounding boxes to the original image size
candidates_scaled = [(int(x * (image.shape[1] / new_width)),
                      int(y * (image.shape[0] / new_height)),
                      int(w * (image.shape[1] / new_width)),
                      int(h * (image.shape[0] / new_height)))
                     for x, y, w, h in candidates]
return candidates_scaled
