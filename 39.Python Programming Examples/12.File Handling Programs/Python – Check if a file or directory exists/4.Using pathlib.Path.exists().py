# Import Path class
from pathlib import Path

# Path
path = '/home/gfg/Desktop'

# Instantiate the Path class
obj = Path(path)

# Check if path points to
# an existing file or directory
print(obj.exists())
