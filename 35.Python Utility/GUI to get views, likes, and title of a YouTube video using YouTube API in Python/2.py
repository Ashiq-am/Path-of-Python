# creating youtube resource object
youtube = build('youtube','v3', developerKey="Enter API Key")

# retrieve youtube video results
video_request=youtube.videos().list(
part='snippet,statistics',
id="Enter Video ID"
)

video_response = video_request.execute()
