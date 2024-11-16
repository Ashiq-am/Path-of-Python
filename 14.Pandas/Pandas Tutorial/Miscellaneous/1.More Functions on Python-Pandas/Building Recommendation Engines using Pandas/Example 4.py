# import pandas library
import pandas as pd

# Get the column names
col_names = ['user_id', 'item_id',
			'rating', 'timestamp']

# Load the dataset
path = 'https://media.geeksforgeeks.org/\
wp-content/uploads/file.tsv'

ratings = pd.read_csv(path, sep='\t',
					names=col_names)

# Check the head of the data
print(ratings.head())

# Check out all the movies and their respective IDs
movies = pd.read_csv(
	'https://media.geeksforgeeks.org/\
	wp-content/uploads/Movie_Id_Titles.csv')
print(movies.head())
