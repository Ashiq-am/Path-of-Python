# import zipfile package
import zipfile

# import the python pandas package
import pandas as pd

# create data_frame1 by creating a dictionary
# in which values are stored as list
data_frame1 = pd.DataFrame({'Fruits': ['Appple', 'Banana', 'Mango',
                                       'Dragon Fruit', 'Musk melon', 'grapes'],
                            'Sales in kg': [20, 30, 15, 10, 50, 40]})

# create data_frame2 by creating a dictionary
# in which values are stored as list
data_frame2 = pd.DataFrame({'Vegetables': ['tomato', 'Onion', 'ladies finger',
                                           'beans', 'bedroot', 'carrot'],
                            'Sales in kg': [200, 310, 115, 110, 55, 45]})

# create data_frame3 by creating a dictionary
# in which values are stored as list
data_frame3 = pd.DataFrame({'Baked Items': ['Cakes', 'biscuits', 'muffins',
                                            'Rusk', 'puffs', 'cupcakes'],
                            'Sales in kg': [120, 130, 159, 310, 150, 140]})

# create data_frame3 by creating a dictionary
# in which values are stored as list
data_frame4 = pd.DataFrame({'Cool drinks': ['Pepsi', 'Coca-cola', 'Fanta',
                                            'Miranda', '7up', 'Sprite'],
                            'Sales in count': [1209, 1230, 1359, 3310, 2150, 1402]})

# specify the path in which the zip file has to be stored
with zipfile.ZipFile("path_to_file.zip", "w") as zf:
    # in open function specify the name in which
    # the excel file has to be stored
    with zf.open("filename.xlsx", "w") as buffer:
        with pd.ExcelWriter(buffer) as writer:
            # use to_excel function and specify the sheet_name and
            # index to store the dataframe in sepecified sheet
            data_frame1.to_excel(writer, sheet_name="Fruits", index=False)
            data_frame2.to_excel(writer, sheet_name="Vegetables", index=False)
            data_frame3.to_excel(writer, sheet_name="Baked Items", index=False)
            data_frame4.to_excel(writer, sheet_name="Cool Drinks", index=False)
