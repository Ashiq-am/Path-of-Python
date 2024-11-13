# Defining a custom transformer class
class CustomTransform(object):
    def __init__(self, split_percent=0.5):
        self.split_percent = split_percent

    # Defining the transform method
    def __call__(self, image):
        # Splitting the image into two parts
        split = int(image.shape[1] * self.split_percent)
        image1 = image[:, :split, :]
        image2 = image[:, split:, :]

        # Returning the two parts of the image
        return image1, image2
