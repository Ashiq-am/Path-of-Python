# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting ogg encoded streams of the video
value = video.oggstreams

# printing the value
print(value)
