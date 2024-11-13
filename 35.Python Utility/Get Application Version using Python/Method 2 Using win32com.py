# Import Module
from win32com.client import *

def get_version_number(file_path):

	information_parser = Dispatch("Scripting.FileSystemObject")
	version = information_parser.GetFileVersion(file_path)
	return version

file_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
version = get_version_number(file_path)

print(version)
