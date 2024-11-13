# import required module
import glob

# assign directory
directory = 'files'

# itrate over files in
# that directory
for filename in glob.iglob(f'{directory}/*'):
	print(filename)
