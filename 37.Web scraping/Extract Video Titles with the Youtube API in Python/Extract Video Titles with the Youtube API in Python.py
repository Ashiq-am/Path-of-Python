from googleapiclient.discovery import build

DEVELOPER_KEY = 'YOUR-API-KEY-HERE'


class Youtube():
    def __init__(self, query, maxResults):
        self.query = query
        self.maxResults = maxResults

    def search_videos(self):
        youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
        request = youtube.search().list(part='id', type='video', q=self.query, maxResults=self.maxResults)
        response = request.execute()
        return response

    def get_video_details(self, count, video_id):
        youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
        request = youtube.videos().list(part='snippet,statistics', id=video_id)
        details = request.execute()
        title = details['items'][0]['snippet']['title']
        print(f'Title of video {count}: {title}')

    def main(self):
        results = self.search_videos()
        video_list = results['items']
        for i in range(len(video_list)):
            video_id = video_list[i]['id']['videoId']
            self.get_video_details(i + 1, video_id)


query = 'Gfg'
maxResults = 10
obj = Youtube(query, maxResults)
obj.main()

# This is contributed by Shraman Jain
