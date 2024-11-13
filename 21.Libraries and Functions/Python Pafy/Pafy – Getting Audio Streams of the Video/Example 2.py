# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = mmjDZGSr7EA"

# getting video
video = pafy.new(url)

# getting audio streams of the video
value = video.audiostreams

# printing the value
print(value)
