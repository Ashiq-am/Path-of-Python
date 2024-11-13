# import libraries
from apiclient.discovery import build
import pprint

# arguments to be passed to build function
DEVELOPER_KEY = "Your_developer_key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating youtube resource object
# for interacting with API
youtube = build(YOUTUBE_API_SERVICE_NAME,
                YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)


def mostpopular_video_details():
    # Call the videos.list method to retrieve video info
    list_videos_byid = youtube.videos().list(
        part="id, snippet, contentDetails, statistics",
        chart='mostPopular', regionCode='IN',
        maxResults=2, videoCategoryId='').execute()

    # extracting the results from search response
    results = list_videos_byid.get("items", [])

    # empty list to store video details
    videos = []
    n = 1
    for result in results:
        videos.append("% s (% s) (% s) (% s) (% s) (% s)"
                      % (n, result["snippet"]["title"],
                         result['snippet']['description'],
                         result["snippet"]["publishedAt"],
                         result['contentDetails'],
                         result["statistics"]))
        n = n + 1

    print("Videos:\n", "\n".join(videos), "\n")


if __name__ == "__main__":
    mostpopular_video_details()
