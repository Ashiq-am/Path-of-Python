import os


def change_owner(path, uid):
    try:
        # Printing the current owner id and group id
        print("File's owner id:", os.stat(path).st_uid)
        print("File's group id:", os.stat(path).st_gid)

        # Setting gid as -1 to leave the group id unchanged
        gid = -1
        os.chown(path, uid, gid)
        print("\nOwner id of the file has been changed successfully, leaving the group id unchanged")

        # Printing the owner id and group id of the file now
        print("\nFile's owner id now is:", os.stat(path).st_uid)
        print("File's group id now is:", os.stat(path).st_gid)

    except FileNotFoundError:
        print("File not found:", path)
    except Exception as e:
        print("An error occurred:", e)


# Example usage
path = "C:\\Users\\Lenovo\\Downloads\\Work TP\\trial.py"
uid = 200
change_owner(path, uid)
