# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting view count of video
value = video.viewcount

# printing the value
print("View Count : " + str(value))
