def create_playlist():
	"""Create A New Playlist"""
	request_body = json.dumps(
		{
			"name": "My New Geeks Playlist",
			"description": "Songs",
			"public": True,
		}
	)

	query = "https://api.spotify.com/v1/users/{}/playlists".format(
		spotify_user_id)
	response = requests.post(
		query,
		data=request_body,
		headers={
			"Content-Type": "application/json",
			"Authorization": "Bearer {}".format("spotify_token"),
		},
	)

	return response["id"]
