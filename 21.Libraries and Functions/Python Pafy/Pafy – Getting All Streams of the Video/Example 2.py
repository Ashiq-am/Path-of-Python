# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = mmjDZGSr7EA"

# getting video
video = pafy.new(url)

# getting allstreams of the video
value = video.allstreams

# printing the value
print(value)
