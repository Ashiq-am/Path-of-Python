# Import Module
from googleapiclient.discovery import build


def playlist_video_links(playlistId):
    nextPageToken = None

    # Creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey='Enter API Key')

    while True:

        # Retrieve youtube video results
        pl_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlistId,
            maxResults=50,
            pageToken=nextPageToken
        )
        pl_response = pl_request.execute()

        # Iterate through all response and get video desription
        for item in pl_response['items']:
            description = item['snippet']['description']

            print(description)

            print("\n")

        nextPageToken = pl_response.get('nextPageToken')

        if not nextPageToken:
            break


playlist_video_links('Enter Playlist ID')
