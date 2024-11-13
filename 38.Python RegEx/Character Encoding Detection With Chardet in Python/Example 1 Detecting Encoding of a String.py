import chardet

# String with unknown encoding
data = b'\xff\xfe\x41\x00\x42\x00\x43\x00'

# Detect the encoding
result = chardet.detect(data)
print(result['encoding'])
