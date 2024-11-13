# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting best video stream of video
value = video.getbestvideo()

# printing the value
print("Best Video Steam : " + str(value))
