import os


def change(path, uid, gid):
    try:
        # Displaying current owner and group IDs
        print("File's owner id:", os.stat(path).st_uid)
        print("File's group id:", os.stat(path).st_gid)

        # Changing the owner id and group id of the file
        os.chown(path, uid, gid)
        print("\nOwner id and group id of the file have been changed successfully")

        # Displaying updated owner and group IDs
        print("\nFile's owner id now is:", os.stat(path).st_uid)
        print("File's group id now is:", os.stat(path).st_gid)

    except FileNotFoundError:
        print("File not found:", path)
    except Exception as e:
        print("An error occurred:", e)


# Example usage
path = "C:\\Users\\Lenovo\\Downloads\\Work TP\\trial.py"
uid = 1500
gid = 1500
change(path, uid, gid)
