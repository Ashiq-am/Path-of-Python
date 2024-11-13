import tempfile as tf

f = tf.mkdtemp(suffix='', prefix='tmp')
print(f)
