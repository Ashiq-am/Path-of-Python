import pafy

# url of video
url = "https://www.youtube.com/watch?v=Ns4LCeeOFS4&t=320s"

# instant created
video = pafy.new(url)

# print title
print(video.title)

# print rating
print(video.rating)

# print viewcount
print(video.viewcount)

# print author & video length
print(video.author, video.length)

# print duration, likes, dislikes & description
print(video.duration, video.likes, video.dislikes, video.description)
