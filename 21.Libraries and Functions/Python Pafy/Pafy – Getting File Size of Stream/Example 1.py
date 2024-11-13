# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting all the available streams
streams = video.allstreams

# selecting one stream
stream = streams[1]
# getting file size of stream
value = stream.get_filesize()

# printing the value
print("File Size in bytes: " + str(value))
