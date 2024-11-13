shutil.copy2(src, dst, follow_symlinks = False)

# To preserve symbolic links in copied directories
shutil.copytree(src, dst, symlinks = True)
