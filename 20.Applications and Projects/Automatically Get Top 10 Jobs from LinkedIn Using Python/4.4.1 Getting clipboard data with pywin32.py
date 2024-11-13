# Library for win32 clipboard api
import win32clipboard


# Get clipboard data
def get_clipboard_data():
    try:

        # Call open clipboard api
        win32clipboard.OpenClipboard()

        # Call get clipboard data api, and return the data
        data = win32clipboard.GetClipboardData()
        return data
    except:

        # If it got exception, return empty string
        return ""
    finally:

        # Call close clipboard api
        win32clipboard.CloseClipboard()
