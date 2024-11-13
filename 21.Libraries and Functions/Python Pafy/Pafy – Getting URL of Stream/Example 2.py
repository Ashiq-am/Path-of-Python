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

# getting url of stream
value = stream.url

# printing the value
print("URL : " + str(value))
