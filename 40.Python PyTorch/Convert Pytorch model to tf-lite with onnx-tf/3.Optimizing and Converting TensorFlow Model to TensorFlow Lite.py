# Step 8: Convert the TensorFlow model to TensorFlow Lite with optimization (quantization)
converter = tf.lite.TFLiteConverter.from_saved_model(tf_model_dir)

# Apply post-training quantization to reduce model size
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # Default quantization


# Convert the model
tflite_model = converter.convert()

# Step 9: Save the optimized TensorFlow Lite model
with open("mnist_model_optimized.tflite", "wb") as f:
    f.write(tflite_model)

print("Optimized TensorFlow Lite model saved successfully!")
