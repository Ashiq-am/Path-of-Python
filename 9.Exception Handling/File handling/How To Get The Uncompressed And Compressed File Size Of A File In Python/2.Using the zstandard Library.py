import os
import zstandard as zstd

def get_file_sizes(file_path):
	# Get the uncompressed size using os.path.getsize()
	uncompressed_size = os.path.getsize(file_path)

	# Get the compressed size using zstandard
	with open(file_path, 'rb') as file:
		compressed_data = zstd.compress(file.read())
		compressed_size = len(compressed_data)

	return uncompressed_size, compressed_size

# Example usage
file_path = r'add\file\path'
uncompressed_size, compressed_size = get_file_sizes(file_path)

print(f'Uncompressed Size: {uncompressed_size} bytes')
print(f'Compressed Size: {compressed_size} bytes')
