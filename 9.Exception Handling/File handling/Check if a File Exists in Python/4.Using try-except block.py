try:
    # File path
    a = "myfile.txt"

    # Try to open the file
    with open(a, 'r') as file:
        print("File exists and is ready to read")
except FileNotFoundError:
    print("File does not exist")