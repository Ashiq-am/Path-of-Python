import os
import zipfile


def get_file_sizes(file_path):
    # Get the uncompressed size using os.path.getsize()
    uncompressed_size = os.path.getsize(file_path)

    # Get the compressed size using zipfile
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        compressed_size = 0

        for entry in zip_file.infolist():
            if not entry.is_dir():
                compressed_size += entry.file_size

    return uncompressed_size, compressed_size


# Example usage
file_path = r'add\file\path'
uncompressed_size, compressed_size = get_file_sizes(file_path)

print(f'Uncompressed Size: {uncompressed_size} bytes')
print(f'Compressed Size: {compressed_size} bytes')
