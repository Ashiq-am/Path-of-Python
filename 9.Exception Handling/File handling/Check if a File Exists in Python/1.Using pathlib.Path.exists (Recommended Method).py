from pathlib import Path

# File path
a = Path("myfile.txt")

# Check if the file exists
if a.exists():
    print("File exists")
else:
    print("File does not exist")