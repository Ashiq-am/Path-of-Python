# Python program to find files
# recursively using Python
import fnmatch
import os

# Using os.walk()
for dirpath, dirs, files in os.walk('src'):

    for filename in files:
        fname = os.path.join(dirpath,filename)

        if fname.endswith('.c'):
            print(fname)

"""
Or
We can also use fnmatch.filter()
to filter out results.
"""
for dirpath, dirs, files in os.walk('src'):
    for filename in fnmatch.filter(files, '*.c'):
        print(os.path.join(dirpath, filename))

# Using os.listdir()
path = "src"
dir_list = os.listdir(path)
for filename in fnmatch.filter(dir_list,'*.c'):
    print(os.path.join(dirpath, filename))
