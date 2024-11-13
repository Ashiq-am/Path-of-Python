# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting video ID
value = video.videoid

# printing the value
print("Video ID : " + value)
