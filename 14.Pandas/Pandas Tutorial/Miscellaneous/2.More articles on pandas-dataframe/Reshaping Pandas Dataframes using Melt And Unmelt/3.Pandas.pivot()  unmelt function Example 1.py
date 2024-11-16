# importing pandas library
import pandas as pd

# creating and initializing a list
values = [[101, 'Rohan', 455, 'Football'],
		[111, 'Elvish', 250, 'Chess'],
		[192, 'Deepak', 495, 'Cricket'],
		[201, 'Sai', 400, 'Ludo'],
		[105, 'Radha', 350, 'Badminton'],
		[118, 'Vansh', 450, 'Badminton']]

# creating a pandas dataframe
df = pd.DataFrame(values,
				columns=['ID', 'Name', 'Marks', 'Sports'])

# displaying the data frame
df
