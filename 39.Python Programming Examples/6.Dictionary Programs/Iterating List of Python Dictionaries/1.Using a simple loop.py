movies = [
	{"title": "The Shawshank Redemption",
		"director": "Frank Darabont", "genre": "Drama", "year": 1994},
	{"title": "The Godfather", "director": "Francis Ford Coppola",
		"genre": "Crime", "year": 1972}
]

# Iterating through the list of dictionaries and unpacking key-value pairs
for movie in movies:
	for key, value in movie.items():
		print(f"{key}: {value}")
