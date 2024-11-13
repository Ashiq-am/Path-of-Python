# Define a function to calculate the SHA-256 hash of a file.
def calculate_hash(file_path):
    # Create a SHA-256 hash object.
    sha256_hash = hashlib.sha256()
    # Open the file in binary mode for reading (rb).
    with open(file_path, "rb") as file:
        # Read the file in 64KB chunks to efficiently handle large files.
        while True:
            data = file.read(65536)  # Read the file in 64KB chunks.
            if not data:
                break
            # Update the hash object with the data read from the file.
            sha256_hash.update(data)
    return sha256_hash.hexdigest()