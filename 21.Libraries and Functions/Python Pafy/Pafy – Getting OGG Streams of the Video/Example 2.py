# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting ogg encoded streams of the video
value = video.oggstreams

# printing the value
print(value)
