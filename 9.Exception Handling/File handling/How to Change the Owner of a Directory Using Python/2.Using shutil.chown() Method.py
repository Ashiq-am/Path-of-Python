import shutil
from pathlib import Path

def change(path, uid, gid):
    try:
        # Getting the owner and the group
        info = Path(path)
        user = info.owner()
        group = info.group()

        print("Present owner and group")
        print("Present owner:", user)
        print("Present group:", group)

        # Changing the owner and the group
        shutil.chown(path, uid, gid)
        print("\nThe owner and the group have been changed successfully")

        # Printing the owner user and group
        info = Path(path)
        user = info.owner()
        group = info.group()
        print("Present owner now:", user)
        print("Present group now:", group)

    except FileNotFoundError:
        print("File not found:", path)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
path = 'C:\\Users\\Lenovo\\Downloads\\Work TP\\trial.py'
uid = 10
gid = 10
change(path, uid, gid)
