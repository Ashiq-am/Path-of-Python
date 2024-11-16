# Import in order to use inbuilt functions
import numpy as np
import pandas as pd
import random

# Define total number of house
number_of_house = 30

# Create data dictionary
data = {'house_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
						14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
						24, 25, 26, 27, 28, 29, 30],
		'number_of_children': [2, 2, 1, 3, 2, 1, 4, 1, 3, 5, 4, 3, 5,
							3, 2, 1, 2, 3, 4, 5, 3, 4, 5, 2, 2, 2,
							2, 3, 2, 1]}

# Transform dictionary into a data frame
df = pd.DataFrame(data)

# Defining Size of Systematic Sample
size_of_systematic_sample = 6

# Defining Interval(gap) in order to get required data.
interval = (number_of_house // size_of_systematic_sample)

# Choosing Random Numner
random_number = random.randint(1, 30)

# Define systematic sampling function
def systematic_sampling(df, step):

	indexes = np.arange(random_number, len(df), step=step)
	systematic_sample = df.iloc[indexes]
	return systematic_sample


# Obtain a systematic sample and save it in a new variable
systematic_sample = systematic_sampling(df, interval)

# View sampled data frame
display(systematic_sample)

# Empty Print Statement for new line
print()

# Save the sample data in a separate variable
systematic_data = round(systematic_sample['number_of_children'].mean())

# Printig Avergae Number of Children
print("Average Number Of Childrens in Locality: ", systematic_data)
