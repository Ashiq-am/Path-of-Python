# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting length of the video
value = video.length

# printing the value
print("Length : " + str(value))
