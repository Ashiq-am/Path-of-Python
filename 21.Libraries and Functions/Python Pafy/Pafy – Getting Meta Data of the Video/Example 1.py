# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting meta data of video
value = video.__repr__()

# printing the value
print("Meta Data : " + value)
