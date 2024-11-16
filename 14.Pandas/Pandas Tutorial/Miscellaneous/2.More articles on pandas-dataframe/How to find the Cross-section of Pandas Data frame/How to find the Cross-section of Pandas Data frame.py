# importing pandas library
import pandas as pd

# Creating a Dictionary
animal_dict = {'num_of_legs': [4, 0, 4, 2, 2, 2],

               'num_of_wings': [0, 0, 0, 2, 2, 2],

               'class': ['Reptiles', 'Reptiles', 'Reptiles',
                         'Birds', 'Birds', 'Birds'],

               'animal': ['Turtle', 'Snake', 'Crocodile',
                          'Parrot', 'Owl', 'Hummingbird'],

               'locomotion': ['swim_walk', 'swim_crawl', 'swim_walk',
                              'flies', 'flies', 'flies']}

# Converting to Data frame and setting index
df = pd.DataFrame(data=animal_dict)
df = df.set_index(['class', 'animal', 'locomotion'])

# Displaying Data frame
df
