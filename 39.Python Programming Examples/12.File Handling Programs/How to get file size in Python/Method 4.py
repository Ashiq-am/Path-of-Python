# approach 4
# using pathlib module
from pathlib import Path

# open file
Path(r'd:/file.jpg').stat()

# getting file size
file=Path(r'd:/file.jpg').stat().st_size

# display the size of the file
print("Size of file is :", file, "bytes")

# this code was contributed by debrc
