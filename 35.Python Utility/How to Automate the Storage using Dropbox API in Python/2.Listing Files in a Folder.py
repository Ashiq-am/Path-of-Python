# explicit function to list files
def list_files_in_folder():
    # here dbx is an object which is obtained
    # by connecting to dropbox via token
    dbx = connect_to_dropbox()

    try:
        folder_path = "/folder_path"

        # dbx object contains all functions that
        # are required to perform actions with dropbox
        files = dbx.files_list_folder(folder_path).entries
        print("------------Listing Files in Folder------------ ")

        for file in files:
            # listing
            print(file.name)

    except Exception as e:
        print(str(e))


list_files_in_folder()
