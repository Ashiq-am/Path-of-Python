import pandas as pd

data = {
	"Anime": ["One Piece", "Naruto", "Bleach",
			"Hunter X Hunter", "Attack On Titan",
			"Gintama", "Code Geass", "Death Note",
			"Black Lagoon", "Classroom Of Elite",
			"Cowboy Bepop", "Jujutsu Kaisen",
			"Blue Period"],
	"Episodes": [1009, 720, 366, 148, 74, 366,
				50, 37, 24, 12, 26, 24, 12],
	"Year": [1999, 2002, 2004, 2011, 2013, 2006,
			2007, 2008, 2006, 2016, 1995,
			2020, 2021]
}
df = pd.DataFrame(data)
