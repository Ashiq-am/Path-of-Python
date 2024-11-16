# import necessary packages
import pandas.api.types

# creating a dictionary
dictionary_obj = {"Geek": 4, "For": 3, "geeks": 5}

pandas.api.types.is_dict_like(dictionary_obj)
