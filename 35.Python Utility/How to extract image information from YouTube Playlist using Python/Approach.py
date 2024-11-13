from distutils.command.build import build

nextPageToken=None

# creating youtube resource object
youtube = build('youtube','v3',developerKey='Enter API Key')

while True:
    # retrieve youtube video results
    pl_request = youtube.playlistItems().list(part='snippet',playlistId=playlistId.get(),maxResults=50, pageToken=nextPageToken)
    pl_response = pl_request.execute()

    nextPageToken = pl_response.get('nextPageToken')


    if not nextPageToken:
        break
