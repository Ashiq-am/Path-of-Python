import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Quit()
print("Excel closed using win32com")
