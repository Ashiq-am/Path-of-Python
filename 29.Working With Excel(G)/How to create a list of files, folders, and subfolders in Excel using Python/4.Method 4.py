import os


# This Function uses os.listdir method to traverse
# folders recursively and appends the name and path of
# file/folders in name_list and path_list respectively.
def find_using_listdir(path, name_list, path_list):
    # Function appends folder name and folder path to
    # name_list and path_list respectively.
    name_list, path_list = append_path_name(path,
                                            name_list, path_list, False)

    for curr_name in os.listdir(path):
        curr_path = os.path.join(path, curr_name)

        # Checks if the current path is a directory.
        if os.path.isdir(curr_path) == True:

            # If the current path is a directory then the
            # function calls itself with the directory path
            # and goes on until a file is found
            find_using_listdir(curr_path, name_list, path_list)
        else:

            # Appends file name and file path to
            # name_list and path_list respectively.
            name_list.append(curr_name)
            path_list.append(curr_path)
    return name_list, path_list


name_list, path_list = find_using_listdir("/content/sample_data", [], [])
print(name_list)
print(path_list)
