# importing pandas as pd
import pandas as pd

# creating the dataframe
df = pd.DataFrame({"A": [14, 4, 5, 4, 1],
                   "B": [5, 2, 54, 3, 2],
                   "C": [20, 20, 7, 3, 8],
                   "D": [14, 3, 6, 2, 6],
                   "E": [23, 45, 64, 32, 23]})

print("Original DataFrame :")
display(df)


# function definition
def highlight_cols(x):
    # copy df to new - original data is not changed
    df = x.copy()

    # select all values to green color
    df.loc[:, :] = 'background-color: green'

    # overwrite values grey color
    df[['B', 'C', 'E']] = 'background-color: grey'

    # return color df
    return df


print("Highlighted DataFrame :")
display(df.style.apply(highlight_cols, axis=None))
