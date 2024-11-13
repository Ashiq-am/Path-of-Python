# importing necessary libraries
import dropbox

# Token Generated from dropbox
TOKEN = "access_token"


# Establish connection
def connect_to_dropbox():
    try:
        dbx = dropbox.Dropbox(TOKEN)
        print('Connected to Dropbox successfully')

    except Exception as e:
        print(str(e))

    return dbx


dbx = connect_to_dropbox()
