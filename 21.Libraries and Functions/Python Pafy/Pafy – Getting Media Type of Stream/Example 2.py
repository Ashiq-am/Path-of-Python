# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting all the available streams
streams = video.allstreams

# selecting one stream
stream = streams[4]

# getting media tyope of stream
value = stream.mediatype

# printing the value
print("Media Type : " + str(value))
