import pandas as pd

#reading csv files
pokemon_names = pd.read_csv("pokemon.csv", usecols = ["Pokemon"],
												squeeze = True)

#usecol is used to use selected columns
#index_col is used to make passed column as index
pokemon_types = pd.read_csv("pokemon.csv", index_col = "Pokemon",
												squeeze = True)

#using pandas map function
new=pokemon_names.map(pokemon_types)

print (new)
