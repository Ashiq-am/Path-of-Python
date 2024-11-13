folder_path = '/Users/arundhutichakraborty/Downloads/C-NMC_Leukemia/testing_data/C-NMC_test_final_phase_data'
X_test = [read_and_crop_image(os.path.join(folder_path, filename))
          for filename in os.listdir(folder_path)]

# Convert the list of images to a NumPy array
X_test = np.stack(X_test, axis=0)
# Reshape the input data to match the model's input shape
X_test_reshaped = X_test.reshape(-1, 100, 100, 1)trained_model = first_model_trained.model

# Make predictions
predicted = trained_model.predict(reshaped_data)
target_names = ['HEM', 'ALL']

# Generate the classification report
print(classification_report(y_test, binary_predictions, target_names=target_names))
