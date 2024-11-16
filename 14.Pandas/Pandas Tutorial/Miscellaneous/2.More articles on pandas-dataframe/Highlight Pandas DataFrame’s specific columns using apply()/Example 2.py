# importing pandas as pd
import pandas as pd

# creating the dataframe
df = pd.DataFrame({"Name": ["Yash", "Ankit", "Rao"],
                   "Age": [5, 2, 54]})

print("Original DataFrame :")
display(df)


# function definition
def highlight_cols(x):
    # copy df to new - original data is not changed
    df = x.copy()

    # select all values to yellow color
    df.loc[:, :] = 'background-color: yellow'

    # return color df
    return df


print("Highlighted DataFrame :")
display(df.style.apply(highlight_cols, axis=None))
