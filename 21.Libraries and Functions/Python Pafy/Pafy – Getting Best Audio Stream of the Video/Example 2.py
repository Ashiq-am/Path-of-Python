# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = i6rhnSoK_gc"

# getting video
video = pafy.new(url)
# getting best audio stream of video
value = video.getbestaudio()

# printing the value
print("Best Audio Stream : " + str(value))
