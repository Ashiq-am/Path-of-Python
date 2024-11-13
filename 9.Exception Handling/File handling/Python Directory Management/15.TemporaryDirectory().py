import tempfile as tf

f = tf.TemporaryDirectory(suffix='', prefix='tmp')
print("Temporary file :", f.name)

f.cleanup()
