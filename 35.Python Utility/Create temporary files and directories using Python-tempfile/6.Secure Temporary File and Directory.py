import tempfile


secure_temp = tempfile.mkstemp(prefix="pre_",suffix="_suf")
print(secure_temp)
