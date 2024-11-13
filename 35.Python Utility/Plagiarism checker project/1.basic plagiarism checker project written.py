import hashlib

def check_plagiarism(file1, file2):
    # Read the contents of the two files
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    # Create hash objects for each file
    hash1 = hashlib.sha256()
    hash2 = hashlib.sha256()

    # Hash the contents of each file
    hash1.update(text1.encode())
    hash2.update(text2.encode())

    # Compare the hashes
    if hash1.hexdigest() == hash2.hexdigest():
        print("The files are identical.")
    else:
        print("The files are different.")

# Example usage
check_plagiarism("file1.txt", "file2.txt")
