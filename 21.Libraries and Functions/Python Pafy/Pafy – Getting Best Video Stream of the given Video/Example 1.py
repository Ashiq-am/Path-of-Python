# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting best video stream of video
value = video.getbestvideo()

# printing the value
print("Best Video Steam : " + str(value))
