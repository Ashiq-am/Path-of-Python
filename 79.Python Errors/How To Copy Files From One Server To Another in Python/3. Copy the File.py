# code
file_to_transfer = '/path/on/source/file.txt'
destination_path = '/path/on/destination/file.txt'

# The actual file transfer
sftp.get(file_to_transfer, destination_path)
