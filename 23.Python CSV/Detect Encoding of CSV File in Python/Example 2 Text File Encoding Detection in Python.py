import chardet

# Step 2: Read CSV File in Binary Mode
with open('exm.txt', 'rb') as f:
	data = f.read()

# Step 3: Detect Encoding using chardet Library
encoding_result = chardet.detect(data)

# Step 4: Retrieve Encoding Information
encoding = encoding_result['encoding']

# Step 5: Print Detected Encoding Information
print("Detected Encoding:", encoding)
