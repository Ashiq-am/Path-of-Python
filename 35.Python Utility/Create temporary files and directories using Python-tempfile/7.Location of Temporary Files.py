import tempfile

tempfile.tempdir = "/temp"
print(tempfile.gettempdir())
