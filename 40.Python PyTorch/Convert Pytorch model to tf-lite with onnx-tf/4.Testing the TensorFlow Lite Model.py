interpreter = tf.lite.Interpreter(model_path="mnist_model_optimized.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Evaluate the TensorFlow Lite model
correct = 0
total = 0

# Loop through test data
for images, labels in test_loader:
    # Convert PyTorch tensor to numpy
    images_np = images.numpy()

    for i in range(len(images_np)):
        input_data = np.expand_dims(images_np[i], axis=0).astype(np.float32)  # Adjust shape for TFLite

        # Set the tensor to the input data
        interpreter.set_tensor(input_details[0]['index'], input_data)

        # Invoke the interpreter
        interpreter.invoke()

        # Get output predictions
        output_data = interpreter.get_tensor(output_details[0]['index'])
        prediction = np.argmax(output_data)

        # Compare prediction to the true label
        if prediction == labels[i].item():
            correct += 1
        total += 1

# Print the accuracy of the optimized TensorFlow Lite model
accuracy = correct / total
print(f'Optimized TensorFlow Lite Model Accuracy: {accuracy * 100:.2f}%')
