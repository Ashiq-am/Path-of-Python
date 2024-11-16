import pandas as pd

# Data
my_data = {"views": [12, 13, 100, 80, 91], "likes": [3, 8, 23, 17, 56]}
my_df = pd.DataFrame(my_data) # DataFrame

# Printing the DataFrame
print(my_df.to_string())

# Calculating the number of views greater than 30
# as well as likes less than 20
sum = sum((my_df.likes < 20) & (my_df.views > 30))
print("Likes less than 20 and Views more than 30: ", sum)
