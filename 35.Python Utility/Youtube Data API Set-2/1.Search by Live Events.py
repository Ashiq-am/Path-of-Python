from apiclient.discovery import build

# Arguments that need to passed to the build function
DEVELOPER_KEY = "Your_API_Key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


def youtube_search_location(query, max_results=2):
    # calling the search.list method to
    # retrieve youtube search results
    search_location = youtube_object.search().list(q=query,
                                                   type='video', eventType='live',
                                                   part="id, snippet",
                                                   maxResults=max_results).execute()

    # extracting the results from search response
    results = search_location.get("items", [])

    # empty list to store video metadata
    videos = []

    # extracting required info
    # from each result object
    for result in results:

        # video result object
        if result['id']['kind'] == "youtube# video":
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                     result["id"]["videoId"], result['snippet']['description'],
                                                     result['snippet']['thumbnails']['default']['url']))

    print("Videos:\n", "\n".join(videos), "\n")


if __name__ == "__main__":
    youtube_search_location('Social Media', max_results=2)
