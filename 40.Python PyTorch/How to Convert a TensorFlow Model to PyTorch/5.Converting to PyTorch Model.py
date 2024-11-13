import onnx
from onnx2pytorch import ConvertModel

# Convert ONNX model to PyTorch
pytorch_model = ConvertModel(onnx_model)
pytorch_model
