# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting dislikes of the video
value = video.dislikes

# printing the value
print(value)
