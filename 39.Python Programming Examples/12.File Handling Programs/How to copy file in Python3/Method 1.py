# copy a file using shutil.copyfile() method
import shutil

# path where original file is located
sourcePath = "c:\\SourceFolder\\gfg.txt"

# path were a copy of file is needed
destinationPath = "c:\\DestinationFolder\\gfgcopy.txt"

# call copyfile() method
shutil.copyfile(sourcePath, destinationPath)
