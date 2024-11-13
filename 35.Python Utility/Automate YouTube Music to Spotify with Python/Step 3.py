def extract_song_from_yt(dic):
	"""Fetch song name from Youtube"""

	url = "https://www.youtube.com/watch?v="
	info = []
	song = ""
	for i in range(len(dic["items"])):

		video_url = url+str(dic["items"][i]["snippet"]
							['resourceId']['videoId'])
		details = youtube_dl.YoutubeDL(
			{}).extract_info(video_url, download=False)
		track, artist = details['track'], details['artist']

		info.append((track,artist))
	return info
