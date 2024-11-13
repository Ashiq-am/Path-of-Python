import tf2onnx

# Convert the model to ONNX format
onnx_model, _ = tf2onnx.convert.from_keras(loaded_model)
