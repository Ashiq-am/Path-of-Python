# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting best thumbnail of video
value = video.getbestthumb()

# printing the value
print("Best Thumbnail: " + str(value))
