# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = 3QKiK4rJIB0"

# getting video
video = pafy.new(url)

# getting description of the video
value = video.description

# printing the value
print("Video description : " + str(value))
