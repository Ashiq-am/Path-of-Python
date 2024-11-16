# Import in order to use inbuilt functions
import numpy as np
import pandas as pd

# Define total number of students
number_of_students = 15

# Create data dictionary
data = {'Id': np.arange(1, number_of_students+1).tolist(),
		'height': [159, 171, 158, 162, 162, 177, 160, 175,
				168, 171, 178, 178, 173, 177, 164]}

# Transform dictionary into a data frame
df = pd.DataFrame(data)


# Define systematic sampling function
def systematic_sampling(df, step):

	indexes = np.arange(0, len(df), step=step)
	systematic_sample = df.iloc[indexes]
	return systematic_sample


# Obtain a systematic sample and save it in a new variable
systematic_sample = systematic_sampling(df, 3)

# View sampled data frame
display(systematic_sample)

# Empty Print Statement for new line
print()

# Save the sample data in a separate variable
systematic_data = round(systematic_sample['height'].mean())
print("Average Height in cm: ", systematic_data)
