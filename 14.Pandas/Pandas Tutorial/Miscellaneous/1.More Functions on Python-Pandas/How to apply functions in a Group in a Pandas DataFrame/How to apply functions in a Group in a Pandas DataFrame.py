# import libraries
import pandas as pd

# set up the data
data_dict = {"Student House": ["Lavender", "Lavender", "Lavender",
                               "Lavender", "Daisy", "Daisy",
                               "Daisy", "Daisy", "Daffodils",
                               "Daffodils", "Daffodils", "Daffodils"],

             "Points": [10, 4, 6, 7, 3, 8, 9, 10, 4, 5, 6, 7]}

data_df = pd.DataFrame(data_dict)
print("Dataframe : ")
data_df
