# necessary import for getting
# directory and filenames
import os
from bs4 import BeautifulSoup

# Get current working directory
directory = os.getcwd()

# for all the files present in that
# directory
for filename in os.listdir(directory):

    # check whether the file is having
    # the extension as html and it can
    # be done with endswith function
    if filename.endswith('.html'):

        # os.path.join() method in Python join
        # one or more path components which helps
        # to exactly get the file
        fname = os.path.join(directory, filename)
        print("Current file name ..", os.path.abspath(fname))

        # open the file
        with open(fname, 'r') as file:

            beautifulSoupText = BeautifulSoup(file.read(), 'html.parser')

            # parse the html as you wish
            for tag in beautifulSoupText.findAll(True):
                print(tag.name, " : ", len(beautifulSoupText.find(tag.name).text))
