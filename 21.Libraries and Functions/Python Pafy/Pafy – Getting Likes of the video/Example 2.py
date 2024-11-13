# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting likes of the video
value = video.likes

# printing the value
print("Likes : " + str(value))
