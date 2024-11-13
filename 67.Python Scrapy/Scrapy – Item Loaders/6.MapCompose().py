# Import MapCompose processor
from itemloaders.processors import MapCompose


# custom function to filter star
def filter_star(x):
    # return None if 'star' is present
    return None if x == 'star' else x


# Assign the functions to MapCompose
proc = MapCompose(filter_star, str.upper)

# pass arguments and print result
print(proc(['twinkle', 'little', 'star', 'wonder', 'they']))
