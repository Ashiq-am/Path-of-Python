import os


class TempFile:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'w') as f:
            f.write('Temporary data')

    def __del__(self):
        print(f"Deleting temporary file: {self.filename}")
        os.remove(self.filename)


# Creating a temporary file
temp_file = TempFile('temp.txt')
print("Temp file created")

# Deleting the object explicitly (calls __del__ method)
del temp_file
