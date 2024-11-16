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

# create a excel writer object as shown using
# Excelwriter function
with pd.ExcelWriter("path_to_file.xlsx", mode="a", engine="openpyxl") as writer:
    # use to_excel function and specify the sheet_name and index to
    # store the dataframe in sepecified sheet
    data_frame4.to_excel(writer, sheet_name="Cool drinks")
