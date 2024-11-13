# importing pafy
import pafy

# url of playlist
url = "https://www.youtube.com / playlist?list = PLqM7alHXFySE71A2bQdYp37vYr0aReknt"

# getting playlist
playlist = pafy.get_playlist(url)

# selecting single item
item = items[1]

# getting pafy object
i_pafy = item['pafy']

# printing pafy object
print(i_pafy)
