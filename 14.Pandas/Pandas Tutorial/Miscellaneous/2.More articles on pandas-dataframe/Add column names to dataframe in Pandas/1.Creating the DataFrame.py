# importing the pandas library
import pandas as pd

# creating lists
l1 =["Amar", "Barsha", "Carlos", "Tanmay", "Misbah"]
l2 =["Alpha", "Bravo", "Charlie", "Tango", "Mike"]
l3 =[23, 25, 22, 27, 29]
l4 =[69, 54, 73, 70, 74]

# creating the DataFrame
team = pd.DataFrame(list(zip(l1, l2, l3, l4)))

# displaying the DataFrame
print(team)
