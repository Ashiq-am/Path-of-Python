# Import in order to use inbuilt functions
import numpy as np
import pandas as pd
import random

# Define total number of boxes
number_of_boxes = 30

# Create data dictionary
data = {'Box_Number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                       15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30],

        'Defective_Bulbs': [2, 2, 1, 0, 2, 1, 0, 1, 3, 5, 4, 3, 5, 3,
                            0, 1, 2, 0, 4, 5, 3, 4, 5, 2, 0, 3, 2, 0,
                            5, 4]}

# Transform dictionary into a data frame
df = pd.DataFrame(data)

# Size of Systematic Sample
size_systematic_sample = 5

# Interval (Gap) taken
interval = (number_of_boxes // size_systematic_sample)

# Choosing Random Starting Point
random_number = random.randint(1, 30)


# Define systematic sampling function
def systematic_sampling(df, step):
    indexes = np.arange(random_number, len(df) - 1, step=step)
    systematic_sample = df.iloc[indexes]
    return systematic_sample


# Obtain a systematic sample and save it in a new variable
systematic_sample = systematic_sampling(df, interval)

# View sampled data frame
display(systematic_sample)

# Empty Print Statement for new line
print()

# Save the sample data in a separate variable
systematic_data = round(systematic_sample['Defective_Bulbs'].mean())

# Printig Avergae Number of Defective Bulbs
print("Average Number Of Defective Bulbs: ", systematic_data)
