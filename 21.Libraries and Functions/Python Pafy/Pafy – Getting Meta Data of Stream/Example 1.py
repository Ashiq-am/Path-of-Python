# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting all the available streams
streams = video.allstreams

# getting meta data of stream
value = stream.__repr__()

# printing the value
print("Meta Data : " + str(value))
