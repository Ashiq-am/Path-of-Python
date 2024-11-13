# use read_csv method to read
# entire data from the file
data = pandas.read_csv('Indian_States_Coordinates - Sheet1.csv')

# extract the values under "State"
# column and convert it to a list
states = data['State'].to_list()

# make an empty list of correct guesses,
# that we will use to see how many
# correct guesses the user makes while
# playing the game.
correct_guesses = []
