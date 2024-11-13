import os

file_path = 'example.txt'
file_info = os.stat(file_path)
file_size_bytes = file_info.st_size

# Conversion to kilobytes, megabytes, and gigabytes
file_size_kb = file_size_bytes / 1024
file_size_mb = file_size_kb / 1024
file_size_gb = file_size_mb / 1024

print(f"File Size (Bytes): {file_size_bytes} B")
print(f"File Size (KB): {file_size_kb:.2f} KB")
print(f"File Size (MB): {file_size_mb:.2f} MB")
print(f"File Size (GB): {file_size_gb:.2f} GB")
