import tempfile

temp = tempfile.NamedTemporaryFile(prefix='pre_', suffix='_suf')
print(temp.name)
