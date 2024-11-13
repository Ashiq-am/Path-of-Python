import glob


# This Function uses glob.iglob method to traverse
# folders recursively and appends the name and path of
# file/folders in name_list and path_list respectively.
def find_using_glob(path, name_list, path_list):
    # Appends the Parent Directory name and path
    # and modifies the parent path so that iglob
    # can traverse recursively.
    path, name_list, path_list = append_path_name(
        path, name_list, path_list, True)

    # glob.iglob with recursive set to True will
    # get all the file/folder paths.
    for curr_path in glob.iglob(path, recursive=True):
        # Appends file/folder name and path to
        # name_list and path_list respectively.
        name_list, path_list = append_path_name(
            curr_path, name_list, path_list, False)

    return name_list, path_list


name_list, path_list = find_using_glob("/content/sample_data", [], [])
print(name_list)
print(path_list)
