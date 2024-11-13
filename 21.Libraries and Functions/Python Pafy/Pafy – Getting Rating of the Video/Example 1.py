# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting rating of the video
value = video.rating

# printing the value
print("Rating : " + str(value))
