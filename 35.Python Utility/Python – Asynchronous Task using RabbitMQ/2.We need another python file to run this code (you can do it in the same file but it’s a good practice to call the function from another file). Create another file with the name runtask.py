import sys
from task_queue import download

# gets the first command line argument
link = sys.argv[1]

# gets the second command line argument
filename = sys.argv[2]

# calling the download function
download.delay(link, filename)
