# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting all the available streams
streams = video.allstreams

# selecting one stream
stream = streams[7]

# getting itag of the stream
value = stream.itag

# printing the value
print("Itag : " + str(value))
