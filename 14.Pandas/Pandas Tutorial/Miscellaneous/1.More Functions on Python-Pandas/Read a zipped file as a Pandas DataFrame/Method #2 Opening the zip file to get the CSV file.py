# import required modules
import zipfile
import pandas as pd

# oppen zipped dataset
with zipfile.ZipFile("test.zip") as z:
    # open the csv file in the dataset

    with z.open("test.csv") as f:
        # read the dataset
        train = pd.read_csv(f)

        # display dataset
        print(train.head())
