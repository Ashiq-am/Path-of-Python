import os

print("Enter 'quit' for exiting the program")
filename = input('Enter the name of the file, that is to be deleted : ')
if filename == 'quit':
    exit()
else:
    print('\nStarting the removal of the file !')
    os.remove(filename)

    print('\nFile, ', filename, 'The file deletion is successfully completed !!')


