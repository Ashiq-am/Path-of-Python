import hashlib


def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()


file_path = "GFG.txt"  # Path to your file
md5_hash = calculate_md5(file_path)
print("MD5 hash of the file:", md5_hash)
