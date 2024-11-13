# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)

# getting best stream of video
value = video.getbest()

# printing the value
print("Best Stream : " + str(value))
