# Import Module
from googleapiclient.discovery import build

# Create YouTube Object
youtube = build('youtube', 'v3',
				developerKey='Enter API key')

# Get video count
def Channel_Depth_details(channel_id):
	pl_request = youtube.playlists().list(
		part='contentDetails,snippet',
		channelId='channel_id',
		maxResults=50
	)
	pl_response = pl_request.execute()

	return len(pl_response['items'])


print(Channel_Depth_details("Channel ID"))
