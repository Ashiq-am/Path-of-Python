# Import Path class
from pathlib import Path

# Path
path = '/home/ihritik/Desktop'

# Instantiate the Path class
obj = Path(path)

# Check if path refers to
# directory or not
print(obj.is_dir())
