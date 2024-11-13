# importing the module
import glob

# accesing and printing files in directory and subdirectory
for filename in glob.glob('D:\\AllData\\**\\*.exe', recursive=True):
	print(filename) # print file name
