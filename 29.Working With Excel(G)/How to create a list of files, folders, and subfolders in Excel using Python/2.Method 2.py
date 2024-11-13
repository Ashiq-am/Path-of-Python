import os


# This Function uses os.walk method to traverse folders
# recursively and appends the name and path of file/
# folders in name_list and path_list respectively.
def find_using_os_walk(path, name_list, path_list):
    for root, _, files in os.walk(path):

        # Function returns modified name_list and
        # path_list.
        name_list, path_list = append_path_name(
            root, name_list, path_list, False)

        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Appends file name and file path to
            # name_list and path_list respectively.
            name_list.append(file_name)
            path_list.append(file_path)
    return name_list, path_list


name_list, path_list = find_using_os_walk("/content/sample_data", [], [])
print(name_list)
print(path_list)
