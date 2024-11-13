def predict_and_display(input_image_path, model_path='best_model.h5', threshold=0.5):
	# Load the trained model
	loaded_model = load_model(model_path)

	# Preprocess the input image
	input_image = read_and_crop_image(input_image_path) # Use your image preprocessing function
	input_image = input_image / 255.0 # Assuming pixel values are in the range [0, 255]

	# Make predictions
	predictions = loaded_model.predict(np.expand_dims(input_image, axis=0))

	# Apply thresholding
	binary_predictions = np.where(predictions > threshold, 1, 0)

	# Display the image and predictions
	plt.imshow(input_image)
	if binary_predictions[0] == 1:
		plt.title('Prediction: ALL')
	else:
		plt.title('Prediction: 0')
	plt.show()

# Example usage
input_image_path = '/Users/arundhutichakraborty/Downloads/C-NMC_Leukemia/testing_data/C-NMC_test_final_phase_data/2.bmp'
predict_and_display(input_image_path)
