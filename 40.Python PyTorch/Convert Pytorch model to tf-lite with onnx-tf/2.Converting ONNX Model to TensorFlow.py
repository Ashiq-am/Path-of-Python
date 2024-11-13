onnx_model = onnx.load(onnx_filename)
tf_rep = prepare(onnx_model)

tf_model_dir = "./tf_model"
tf_rep.export_graph(tf_model_dir)
