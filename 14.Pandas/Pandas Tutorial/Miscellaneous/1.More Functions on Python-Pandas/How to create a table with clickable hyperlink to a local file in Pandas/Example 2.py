# Step 1 : Importing required modules
import pandas as pd
import os

# Step 2 : Creating dataset of files
dataset = [dict(
    file_names='Crop File', location=r'ML/Crop File prep.ipynb'),

    dict(
        file_names='Final Dataset', location=r'ML/FinalData csv creation.ipynb'),

    dict(
        file_names='EDA', location=r'ML/EDA on FinalData csv.ipynb'),

    dict(
        file_names='Model Training', location=r'ML/Model Training.ipynb'),

    dict(
        file_names='Yield Prediction', location=r'ML/yield prediction.ipynb')]

# Step 3 : Converting list into dataframe
df = pd.DataFrame(data)


# Function to convert file path into
# clickable hyperlink form.
def fun(path):
    # returns the final component of a path
    f_url = os.path.basename(path)

    # convert the path into clickable hyperlink
    return '<a href="{}">{}</a>'.format(path, f_url)


# Step 4 : applying make_clikable function
# on column path.
df = df.style.format({'location': fun})

# Step 5 : Finally printing Dataframe
df
