def get_spotify_uri(track, artist):
	"""Search For the Song"""

	query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track".format(
		track,
		artist
	)
	response = requests.get(
		query,
		headers={
			"Content-Type": "application/json",
			"Authorization": "Bearer {}".format("spotify_token")
		}
	)
	songs = response["tracks"]["items"]

	url = songs[0]["uri"]

	return url
