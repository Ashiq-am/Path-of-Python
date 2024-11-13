from instagramy import Instalysis

# Instagram user_id of ipl teams
teams = ["chennaiipl", "mumbaiindians",
		"royalchallengersbangalore", "kkriders",
		"delhicapitals", "sunrisershyd",
		"kxipofficial"]

data = Instalysis(teams)

# return the dataframe
data_frame = data.analyis()
data_frame
