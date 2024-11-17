image = cv2.imread('digit.png', cv2.IMREAD_GRAYSCALE)

# Resize the image to 28x28
image = cv2.resize(image, (28, 28))

# Invert the colors
image = cv2.bitwise_not(image)

# Normalize the image
image = image.astype('float32') / 255

# Reshape the image
image = np.expand_dims(image, axis=0)
image = np.expand_dims(image, axis=-1)

# Predict the digit
prediction = np.argmax(model.predict(image))

print("Predicted Digit:", prediction)
