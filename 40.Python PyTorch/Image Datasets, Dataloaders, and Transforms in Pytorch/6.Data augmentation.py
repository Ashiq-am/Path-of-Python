# Defining a custom augmentation class
class CustomAugmentation(object):
    def __init__(self, flip_prob=0.5, jitter_prob=0.5):
        self.flip_prob = flip_prob
        self.jitter_prob = jitter_prob

    # Defining the transform method
    def __call__(self, image):
        # Flipping the image horizontally
        if np.random.random() < self.flip_prob:
            image = np.flip(image, axis=1)

        # Applying random color jitter by adding random noise
        if np.random.random() < self.jitter_prob:
            image = np.array(image, dtype=np.int32)
            # Adding random noise to the image
            image = image + np.random.randint(-50, 50, size=image.shape, dtype=np.int32)

        # Returning the augmented image
        return image
