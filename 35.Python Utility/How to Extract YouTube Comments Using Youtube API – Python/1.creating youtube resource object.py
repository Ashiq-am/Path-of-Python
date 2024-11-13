# creating youtube resource object
youtube = build('youtube','v3',
				developerKey="Enter API Key")

# retrieve youtube video results
video_response=youtube.commentThreads().list(
part='snippet,replies',
videoId="Enter Video ID"
).execute()
