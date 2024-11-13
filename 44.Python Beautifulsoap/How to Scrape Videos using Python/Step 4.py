for video_tag in video_tags:
	video_url = video_tag.find("a")['href']
	print(video_url)
