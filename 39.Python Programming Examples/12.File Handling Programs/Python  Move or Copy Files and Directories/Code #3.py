
""""""

"""

def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('.pyc')]


shutil.copytree(src, dst, ignore = ignore_pyc_files)

"""