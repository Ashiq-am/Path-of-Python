# Importing required libraries
import pandas as pd

# Creating DataFrame having 4 columns and but
# the data is in unregularized way.
df = pd.DataFrame({'Names': [' Sunny', 'Bunny', 'Ginny ',
                             ' Binny ', ' Chinni', 'Minni'],

                   'Age': [23, 44, 23, 54, 22, 11],

                   'Blood_Group': [' A+', ' B+', 'O+', 'O-',
                                   ' A-', 'B-'],

                   'Gender': [' M', ' M', 'F', 'F', 'F', ' F']
                   })


# Creating a function which will remove extra leading
# and tailing whitespace from the data.
# pass dataframe as a parameter here
def whitespace_remover(dataframe):
    # iterating over the columns
    for i in dataframe.columns:

        # checking datatype of each columns
        if dataframe[i].dtype == 'object':

            # applying strip function on column
            dataframe[i] = dataframe[i].map(str.strip)
        else:

            # if condn. is False then it will do nothing.
            pass


# applying whitespace_remover function on dataframe
whitespace_remover(df)

# printing dataframe
print(df)
