# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting duration of the video
value = video.duration

# printing the value
print("Duration : " + value)
