# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)
# getting video streams of the video
value = video.streams

# printing the value
print("Streams : " + str(value))
