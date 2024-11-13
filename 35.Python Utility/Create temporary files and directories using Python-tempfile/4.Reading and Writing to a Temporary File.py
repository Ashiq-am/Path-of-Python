import tempfile

temp = tempfile.TemporaryFile()
temp.write(b'foo bar')
temp.seek(0)
print(temp.read())

temp.close()
