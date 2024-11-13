# importing pafy
import pafy

# url of playlist
url = "https://www.youtube.com / playlist?list = PLqM7alHXFySGqCvcwfqqMrteqWukz9ZoE"

# getting playlist
playlist = pafy.get_playlist(url)

# prinintg playlist ID
i_d = playlist["playlist_id"]

print(i_d)
