# creating the SIFT algorithm
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp_image, desc_image =sift.detectAndCompute(img, None)

# intializing the dictionary
index_params = dict(algorithm = 0, trees = 5)
search_params = dict()

# by using Flann Matcher
flann = cv2.FlannBasedMatcher(index_params, search_params)
