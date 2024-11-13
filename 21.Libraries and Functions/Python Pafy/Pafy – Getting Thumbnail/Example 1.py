# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting thumbnail of the video
value = video.thumb

# printing the value
print("Thumbnail : " + value)
