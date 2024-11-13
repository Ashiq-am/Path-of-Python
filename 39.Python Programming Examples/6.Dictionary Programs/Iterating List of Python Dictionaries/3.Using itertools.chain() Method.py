from itertools import chain
movies = [
	{"title": "The Shawshank Redemption",
		"director": "Frank Darabont", "genre": "Drama", "year": 1994},
	{"title": "The Godfather", "director": "Francis Ford Coppola",
		"genre": "Crime", "year": 1972},
	{"title": "Inception", "director": "Christopher Nolan",
		"genre": "Sci-Fi", "year": 2010},
	{"title": "Pulp Fiction", "director": "Quentin Tarantino",
		"genre": "Crime", "year": 1994}
]

# Iterating through the list of dictionaries and unpacking key-value pairs
for key, value in chain.from_iterable(d.items() for d in movies):
	print(key, value)
