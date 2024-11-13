import hashlib
import os

def md5(file_path):
    # Calculate the MD5 hash of a file.
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def find_md5_hashes(directory):
    # Find MD5 hashes of files recursively in a directory.
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            hashes[file_path] = md5(file_path)
    return hashes

# Printing Hashes
directory_path = r"C:\Users\shrav\Desktop\GFG"
file_hashes = find_md5_hashes(directory_path)
for file_path, md5_hash in file_hashes.items():
    print(f'File: {file_path}, MD5: {md5_hash}')
