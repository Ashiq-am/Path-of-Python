import tempfile

secure_temp_dir = tempfile.mkdtemp(prefix="pre_",suffix="_suf")
print(secure_temp_dir)
