import chardet

# Read the text file
with open('utf-8.txt', 'rb') as f:
    data = f.read()

# Detect the encoding
result = chardet.detect(data)
print(result['encoding'])
