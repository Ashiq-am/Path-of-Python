def threading():
	# Call download_videos function
	t1 = Thread(target=download_videos)
	t1.start()


def download_videos():
	# Create API Object
	api = Api(api_key='Enter API Key')

	if "youtube" in playlistId.get():
		playlist_id = playlistId.get()[len(
			"https://www.youtube.com/playlist?list="):]
	else:
		playlist_id = playlistId.get()

	# Get list of video links
	playlist_item_by_id = api.get_playlist_items(
		playlist_id=playlist_id, count=None, return_json=True)

	# Iterate through all video links
	for index, videoid in enumerate(playlist_item_by_id['items']):

		link = f"https://www.youtube.com/watch?v={videoid['contentDetails']['videoId']}"

		yt_obj = YouTube(link)

		filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

		# download the highest quality video
		filters.get_highest_resolution().download()

		print(f"Downloaded:- {link}")

	messagebox.showinfo("Success", "Video Successfully downloaded")
