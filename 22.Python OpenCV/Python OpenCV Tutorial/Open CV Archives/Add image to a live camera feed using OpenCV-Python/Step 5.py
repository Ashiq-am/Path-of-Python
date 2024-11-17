# Region of Interest (ROI), where we want
# to insert logo
roi = frame[-size-10:-10, -size-10:-10]

# Set an index of where the mask is
roi[np.where(mask)] = 0
roi += logo
