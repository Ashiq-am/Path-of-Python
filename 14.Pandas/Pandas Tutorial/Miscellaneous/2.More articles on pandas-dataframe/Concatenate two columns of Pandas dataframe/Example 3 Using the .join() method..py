# importing the module
import pandas as pd

# creating 2 DataFrames
location = pd.DataFrame({'area' : ['new-york', 'columbo', 'mumbai']})
food = pd.DataFrame({'food': ['pizza', 'crabs', 'vada-paw']})

# concatenating the DataFrames
dt = location.join(food)

# displaying the DataFrame
print(dt)
