# importing pafy
import pafy

# url of playlist
url = "https://www.youtube.com / playlist?list = PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE"

# getting playlist
playlist = pafy.get_playlist(url)

# pgetting playlist title
title = playlist["title"]

# printing title
print("Title : " + title)
