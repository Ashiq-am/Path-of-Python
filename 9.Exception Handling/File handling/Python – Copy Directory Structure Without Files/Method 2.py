# importing the os module
import os


# defining a function for the task
def create_dirtree_without_files(src, dst):
    # getting the absolute path of the source
    # direcrory
    src = os.path.abspath(src)

    # making a variable having the index till which
    # src string has directory and a path separator
    src_prefix = len(src) + len(os.path.sep)

    # making the destination directory
    os.makedirs(dst)

    # doing os walk in source directory
    for root, dirs, files in os.walk(src):
        for dirname in dirs:
            # here dst has destination directory,
            # root[src_prefix:] gives us relative
            # path from soruce directory
            # and dirname has folder names
            dirpath = os.path.join(dst, root[src_prefix:], dirname)

            # making the path which we made by
            # joining all of the above three
            os.mkdir(dirpath)


# calling the above function
create_dirtree_without_files('D:/projects/base/Structure',
                             'D:/projects/base/copied_structure')
