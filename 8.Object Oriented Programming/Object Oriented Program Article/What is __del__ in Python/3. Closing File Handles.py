class FileHandler:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.file.write("Some initial data")
        print("File opened and written to")

    def __del__(self):
        print("Closing file")
        self.file.close()

# Creating a FileHandler object
file_handler = FileHandler('example.txt')

# Deleting the object explicitly (calls __del__ method)
del file_handler
