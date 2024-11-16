# Step 1 : Importing required modules
import pandas as pd
import os

# Step 2 : Creating dataset of local path images
dataset = [dict(Images='img1', location=r'New/gfg.png'),
           dict(Images='img2', location=r'New/1.png'),
           dict(Images='img3', location=r'New/gfg2.png'),
           dict(Images='img4', location=r'New/oled.png'),
           dict(Images='img5', location=r'New/oled2.png')]

# Step 3 : Converting list into dataframe
df = pd.DataFrame(dataset)


# Function to convert file path into clickable form.


def fun(path):
    # returns the final component of a path
    f_url = os.path.basename(path)

    # convert the path into clickable link
    return '<a href="{}">{}</a>'.format(path, f_url)


# applying function "fun" on column "location".
df = df.style.format({'location': fun})

# Step 5 : Finally printing Dataframe
df
