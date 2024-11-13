def add_song(playlist_id, urls):
	"""Add all songs into the new Spotify playlist"""

	request_data = json.dumps(urls)

	query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
		playlist_id)

	response = requests.post(
		query,
		data=request_data,
		headers={
			"Content-Type": "application/json",
			"Authorization": "Bearer {}".format("spotify_token")
		}
	)

	return response
