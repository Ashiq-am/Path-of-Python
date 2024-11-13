# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting m4a encoded streams of the video
value = video.m4astreams

# printing the value
print(value)
