# import necessary libraries
import pandas as pd
import os
import glob

# use glob to get all the csv files
# in the folder
from Tools.scripts.dutree import display

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

# loop over the list of csv files
for f in csv_files:
    # read the csv file
    df = pd.read_excel(f)

    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

    # print the content
    print('Content:')
    display(df)
    print()
